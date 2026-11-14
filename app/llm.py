"""Optional OpenAI-compatible model for any language and for reading a paper."""

from __future__ import annotations

import json
import os
import re

import httpx

from app.guides import DISCLAIMER, HELP, is_emergency, language_key

SYSTEM = """You are Kanoon Saathi, a voice guide for people in India who may not read, especially farmers and women who want to know their options before they go to a lawyer or a police station.

Rules:
- You are not their lawyer. You do not decide the case. You do not tell them to sign or not to sign.
- Explain what the situation or the paper is, in short spoken sentences, in the language requested.
- Use everyday words. No Latin legal maxims. No act section numbers. If you are not sure of a form name, say the office instead.
- Land records and court practice depend on the state. Say that plainly when land is involved.
- urgency is "now" only if they may be hurt, trapped, or attacked today. A land dispute or a frightening post without immediate danger is "soon". A bill or a request to understand a paper is "learn", unless a court date is close, then "soon".
- For a signature, list what a free District Legal Services Authority lawyer should check before they sign. Tell them they can say they will answer after a lawyer has read it.
- An electricity or water bill is a demand for payment. It does not by itself sell a house or land. A form that changes the name on a meter, or gives away land, is different.
- Mask identity numbers and bank numbers. Keep at most the last four digits.
- Never suggest violence, forged papers, or hiding evidence.
- Official help you may name: 112 emergency, 181 women helpline, 1930 cyber crime helpline, https://cybercrime.gov.in, District Legal Services Authority at the district court, https://nalsa.gov.in, Tele-Law at a Common Service Centre.
- Reply with one JSON object only, no markdown.
"""

SCHEMA_HINT = """
Return JSON with these keys:
{
  "urgency": "now" | "soon" | "learn",
  "title": "short",
  "spoken": "what to say aloud, at most 120 words, short sentences",
  "what_this_is": "two or three plain sentences",
  "steps": [{"title": "short", "detail": "one or two sentences"}],
  "checks": ["questions to hear before signing, or empty"],
  "bring": ["papers or proof to carry, or empty"],
  "help": [{"name": "", "phone": "112 or null", "url": "or null", "note": ""}],
  "disclaimer": ""
}
Write every string in the requested language.
"""


def model_ready() -> bool:
    return bool(os.environ.get("OPENAI_API_KEY", "").strip())


def _extract_json(text: str) -> dict:
    raw = (text or "").strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?", "", raw).strip()
        raw = re.sub(r"```$", "", raw).strip()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if not match:
            raise
        data = json.loads(match.group(0))
    if not isinstance(data, dict):
        raise ValueError("model did not return an object")
    return data


def _trim_spoken(text: str) -> str:
    text = re.sub(r"\s+", " ", (text or "")).strip()
    if len(text) <= 900:
        return text
    cut = text[:900]
    stop = max(cut.rfind("।"), cut.rfind("."), cut.rfind("?"))
    if stop > 400:
        return cut[: stop + 1]
    return cut


def normalize(data: dict, language: str, source: str) -> dict:
    lang = language_key(language)
    urgency = data.get("urgency")
    if urgency not in {"now", "soon", "learn"}:
        urgency = "soon"
    steps = []
    for item in data.get("steps") or []:
        if isinstance(item, dict) and item.get("title"):
            steps.append({"title": str(item.get("title")), "detail": str(item.get("detail") or "")})
        elif isinstance(item, str):
            steps.append({"title": item, "detail": ""})
    help_items = []
    for item in data.get("help") or []:
        if not isinstance(item, dict) or not item.get("name"):
            continue
        phone = item.get("phone")
        help_items.append(
            {
                "name": str(item.get("name")),
                "phone": str(phone) if phone else None,
                "url": item.get("url") or None,
                "note": str(item.get("note") or ""),
            }
        )
    if not help_items:
        help_items = HELP[lang]
    checks = [str(x) for x in (data.get("checks") or []) if str(x).strip()]
    bring = [str(x) for x in (data.get("bring") or []) if str(x).strip()]
    answered = language if language else ("en-IN" if lang == "en" else "hi-IN")
    return {
        "urgency": urgency,
        "title": str(data.get("title") or ("Your options" if lang == "en" else "आपके रास्ते")),
        "spoken": _trim_spoken(str(data.get("spoken") or data.get("what_this_is") or "")),
        "what_this_is": str(data.get("what_this_is") or ""),
        "steps": steps[:8],
        "checks": checks[:8],
        "bring": bring[:8],
        "help": help_items[:6],
        "disclaimer": str(data.get("disclaimer") or "").strip() or DISCLAIMER[lang],
        "source": source,
        "answered_in": answered,
    }


async def _chat(messages: list, model: str) -> str:
    key = os.environ["OPENAI_API_KEY"].strip()
    base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    payload = {
        "model": model,
        "temperature": 0.2,
        "messages": messages,
        "response_format": {"type": "json_object"},
    }
    async with httpx.AsyncClient(timeout=90) as client:
        response = await client.post(
            f"{base}/chat/completions",
            headers={"Authorization": f"Bearer {key}"},
            json=payload,
        )
        if response.status_code == 400 and "response_format" in response.text:
            payload.pop("response_format")
            response = await client.post(
                f"{base}/chat/completions",
                headers={"Authorization": f"Bearer {key}"},
                json=payload,
            )
        response.raise_for_status()
        body = response.json()
    return body["choices"][0]["message"]["content"]


async def guide_with_model(text: str, language: str, state: str) -> dict:
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
    user = (
        f"Requested language code: {language}\n"
        f"State: {state or 'not given'}\n"
        f"What the person said:\n{text}\n\n"
        f"{SCHEMA_HINT}"
    )
    raw = await _chat(
        [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
        model,
    )
    data = normalize(_extract_json(raw), language, "model")
    if is_emergency(text):
        data["urgency"] = "now"
    return data


async def explain_image(image_data_url: str, language: str, state: str, note: str) -> dict:
    model = os.environ.get("OPENAI_VISION_MODEL") or os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
    user_text = (
        "Read this photo of a paper for someone who may not read. "
        f"Requested language code: {language}. State: {state or 'not given'}. "
        f"What they said about it: {note or 'nothing'}. "
        "Say what kind of paper it is, who it is from, what it asks, any date, and any money. "
        "Mask long identity and account numbers. "
        "If it asks for a signature or thumb impression, fill checks with what a legal-aid lawyer should look at before they sign. "
        "Do not tell them to sign.\n\n"
        f"{SCHEMA_HINT}"
    )
    raw = await _chat(
        [
            {"role": "system", "content": SYSTEM},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_text},
                    {"type": "image_url", "image_url": {"url": image_data_url}},
                ],
            },
        ],
        model,
    )
    return normalize(_extract_json(raw), language, "model")
