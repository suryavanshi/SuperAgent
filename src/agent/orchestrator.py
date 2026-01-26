"""Simple orchestrator stub."""

from .llm_client import LLMClient
from .prompt_builder import build_prompt


def run_once(message: str, client: LLMClient) -> str:
    prompt = build_prompt(message)
    return client.complete(prompt)
