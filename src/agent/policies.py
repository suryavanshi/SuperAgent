"""Policy definitions."""

from dataclasses import dataclass


@dataclass
class Policy:
    name: str
    description: str
