"""Tool registry."""

from dataclasses import dataclass, field
from typing import Callable, Dict


@dataclass
class ToolRegistry:
    tools: Dict[str, Callable[..., str]] = field(default_factory=dict)

    def register(self, name: str, func: Callable[..., str]) -> None:
        self.tools[name] = func

    def run(self, name: str, *args: str) -> str:
        return self.tools[name](*args)
