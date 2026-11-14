"""Gnani Prisma speech-to-text and Timbre text-to-speech."""

from __future__ import annotations

import os

import httpx

STT_URL = "https://api.vachana.ai/stt/v3"
TTS_URL = "https://api.vachana.ai/api/v1/tts/inference"

LANGS = {
    "hi-IN",
    "en-IN",
    "ta-IN",
    "te-IN",
    "kn-IN",
    "ml-IN",
    "mr-IN",
    "pa-IN",
    "bn-IN",
    "gu-IN",
}


def gnani_ready() -> bool:
    return bool(os.environ.get("GNANI_API_KEY", "").strip())


def _key() -> str:
    return os.environ["GNANI_API_KEY"].strip()


async def transcribe(audio: bytes, filename: str, content_type: str, language: str) -> dict:
    code = language if language in LANGS else "indic-auto"
    headers = {"X-API-Key-ID": _key()}
    files = {"audio_file": (filename or "speech.wav", audio, content_type or "audio/wav")}
    model_name = os.environ.get("GNANI_STT_MODEL", "prisma-v3.0")
    data = {"model": model_name, "language_code": code, "format": "transcribe"}
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(STT_URL, headers=headers, files=files, data=data)
    if response.status_code >= 400:
        raise RuntimeError(_error_text(response))
    body = response.json()
    transcript = (body.get("transcript") or "").strip()
    if not transcript:
        raise RuntimeError("No speech detected. Please speak closer to the microphone and try again.")
    return {
        "transcript": transcript,
        "detected_language": body.get("detected_language_code") or code,
    }


async def synthesize(text: str, language: str) -> bytes:
    code = language if language in LANGS else "hi-IN"
    payload = {
        "text": text,
        "voice": os.environ.get("GNANI_TTS_VOICE", "Shivani"),
        "model": os.environ.get("GNANI_TTS_MODEL", "timbre-v3.0"),
        "language": code,
        "speed": float(os.environ.get("GNANI_TTS_SPEED", "0.92")),
        "audio_config": {
            "sample_rate": 24000,
            "num_channels": 1,
            "sample_width": 2,
            "encoding": "linear_pcm",
            "container": "wav",
        },
    }
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            TTS_URL,
            headers={"X-API-Key-ID": _key(), "Content-Type": "application/json"},
            json=payload,
        )
    if response.status_code >= 400:
        raise RuntimeError(_error_text(response))
    content_type = response.headers.get("content-type", "")
    if "json" in content_type:
        raise RuntimeError(_error_text(response))
    if not response.content:
        raise RuntimeError("Gnani returned empty audio")
    return response.content


def _error_text(response: httpx.Response) -> str:
    try:
        body = response.json()
    except Exception:
        body = response.text[:300]
    return f"Gnani error {response.status_code}: {body}"
