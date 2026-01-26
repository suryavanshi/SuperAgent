"""LLM client wrapper."""

from dataclasses import dataclass


@dataclass
class LLMClient:
    provider: str = "openai"

    def complete(self, prompt: str) -> str:
        return f"[stub:{self.provider}] {prompt}"
