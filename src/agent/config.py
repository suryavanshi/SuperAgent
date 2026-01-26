"""Configuration models for the agent runtime."""

from pydantic import BaseModel


class AgentConfig(BaseModel):
    model: str = "gpt-4o-mini"
    temperature: float = 0.2
