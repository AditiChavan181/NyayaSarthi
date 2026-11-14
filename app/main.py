"""Kanoon Saathi — a voice-first guide before a lawyer or the police."""

from __future__ import annotations

import base64
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

load_dotenv()

from app import gnani, llm
from app.guides import document_without_reader, emergency_guide, is_emergency, rule_guide

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "static"

app = FastAPI(title="Kanoon Saathi")
app.mount("/static", StaticFiles(directory=STATIC), name="static")

MAX_AUDIO = 8 * 1024 * 1024
MAX_IMAGE = 7 * 1024 * 1024


class GuideRequest(BaseModel):
    text: str = Field(min_length=1, max_length=4000)
    language: str = "hi-IN"
    state: str = ""


class SpeakRequest(BaseModel):
    text: str = Field(min_length=1, max_length=1200)
    language: str = "hi-IN"


@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC / "index.html", headers={"Cache-Control": "no-cache"})


@app.get("/api/status")
def status() -> dict:
    return {
        "gnani": gnani.gnani_ready(),
        "model": llm.model_ready(),
        "voice": os.environ.get("GNANI_TTS_VOICE", "Shivani") if gnani.gnani_ready() else None,
    }


def attach_note(result: dict, language: str) -> dict:
    asked = (language or "hi-IN").lower()
    answered = (result.get("answered_in") or "hi-IN").lower()
    if asked[:2] != answered[:2]:
        result["language_note"] = (
            "यह जवाब हिन्दी में है। / This answer is in Hindi until a language-model key is added."
        )
    return result


@app.post("/api/guide")
async def guide(body: GuideRequest) -> dict:
    text = body.text.strip()
    if is_emergency(text):
        return attach_note(emergency_guide(body.language), body.language)
    if llm.model_ready():
        try:
            return attach_note(await llm.guide_with_model(text, body.language, body.state), body.language)
        except Exception:
            fallback = rule_guide(text, body.language, body.state)
            fallback["model_error"] = True
            return attach_note(fallback, body.language)
    return attach_note(rule_guide(text, body.language, body.state), body.language)


@app.post("/api/listen")
async def listen(
    audio: UploadFile = File(...),
    language: str = Form("hi-IN"),
) -> dict:
    if not gnani.gnani_ready():
        raise HTTPException(status_code=503, detail="Gnani key is not set. Use the phone's speech recognition.")
    data = await audio.read()
    if not data:
        raise HTTPException(status_code=400, detail="Empty audio")
    if len(data) > MAX_AUDIO:
        raise HTTPException(status_code=413, detail="Audio is too long")
    try:
        return await gnani.transcribe(data, audio.filename or "speech.wav", audio.content_type or "audio/wav", language)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.post("/api/speak")
async def speak(body: SpeakRequest) -> Response:
    if not gnani.gnani_ready():
        raise HTTPException(status_code=503, detail="Gnani key is not set. The phone voice will speak.")
    try:
        audio = await gnani.synthesize(body.text.strip(), body.language)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return Response(content=audio, media_type="audio/wav")


@app.post("/api/document")
async def document(
    image: UploadFile = File(...),
    language: str = Form("hi-IN"),
    state: str = Form(""),
    note: str = Form(""),
) -> dict:
    data = await image.read()
    if not data:
        raise HTTPException(status_code=400, detail="Empty image")
    if len(data) > MAX_IMAGE:
        raise HTTPException(status_code=413, detail="Image is too large")
    content_type = image.content_type or ""
    if not content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Send a photo of the paper")
    if is_emergency(note):
        return emergency_guide(language)
    if not llm.model_ready():
        return attach_note(document_without_reader(language), language)
    encoded = base64.b64encode(data).decode("ascii")
    data_url = f"{content_type};base64,{encoded}"
    data_url = f"data:{data_url}"
    try:
        result = attach_note(await llm.explain_image(data_url, language, state, note.strip()), language)
    except Exception:
        fallback = document_without_reader(language)
        fallback["model_error"] = True
        return attach_note(fallback, language)
    if is_emergency(result.get("spoken", "")):
        result["urgency"] = "now"
    return result
