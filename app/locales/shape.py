"""Small helpers so every language guide has the same shape."""

from __future__ import annotations


def step(title: str, detail: str) -> dict:
    return {"title": title, "detail": detail}


def guide(
    urgency: str,
    title: str,
    spoken: str,
    what: str,
    steps: list,
    bring: list | None = None,
    checks: list | None = None,
) -> dict:
    return {
        "urgency": urgency,
        "title": title,
        "spoken": spoken,
        "what": what,
        "steps": steps,
        "bring": bring or [],
        "checks": checks or [],
    }
