from agent.llm_client import LLMClient
from agent.orchestrator import run_once


def test_orchestrator_returns_response():
    client = LLMClient(provider="stub")
    result = run_once("hello", client)
    assert "hello" in result
