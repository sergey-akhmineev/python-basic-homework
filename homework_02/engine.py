"""
create dataclass `Engine`
"""
from dataclasses import dataclass, field


@dataclass
class Engine:
    volume:  int
    pistons: int