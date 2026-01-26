"""Prompt builder helpers."""


def build_prompt(message: str) -> str:
    return f"User: {message}\nAssistant:"
