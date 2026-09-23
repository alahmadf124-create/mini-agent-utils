"""Lightweight utility helpers for local AI agents and LLM wrappers."""

from __future__ import annotations

from datetime import datetime, timezone
import json
from typing import Any


class PromptFormatter:
    """Utility class for formatting chat messages into a prompt string."""

    @staticmethod
    def format_messages(
        messages: list[dict[str, Any]], system_prompt: str | None = None
    ) -> str:
        """Format chat messages and an optional system prompt into one string."""
        segments: list[str] = []

        if system_prompt:
            segments.append(f"[SYSTEM]\n{system_prompt.strip()}")

        for message in messages:
            role = str(message.get("role", "unknown")).strip().upper()
            content = str(message.get("content", "")).strip()
            segments.append(f"[{role}]\n{content}")

        return "\n\n".join(segment for segment in segments if segment)


class AgentLogger:
    """Utility class for structured, timestamped local agent logging."""

    @staticmethod
    def log_event(event_type: str, details: dict[str, Any]) -> None:
        """Print a UTC timestamped log line with event type and JSON details."""
        timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        payload = json.dumps(details, ensure_ascii=False, sort_keys=True)
        print(f"[{timestamp}] [{event_type}] {payload}")
