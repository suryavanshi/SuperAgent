"""Transcript storage."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Transcript:
    entries: List[str] = field(default_factory=list)

    def add(self, entry: str) -> None:
        self.entries.append(entry)

    def render(self) -> str:
        return "\n".join(self.entries)
