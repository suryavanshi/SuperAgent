"""Runtime entry points."""

from .config import AgentConfig
from .llm_client import LLMClient
from .orchestrator import run_once


def run(message: str, config: AgentConfig | None = None) -> str:
    config = config or AgentConfig()
    client = LLMClient()
    return run_once(message, client)
