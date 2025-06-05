from dataclasses import dataclass, field, fields
from typing import List

from code.data.Translation import Translation

@dataclass
class Word:
    name: str = field(default="")
    transcription: str = field(default="")
    translations:List[Translation] = field(default_factory=list)
    skill: int = field(default=0)
    correct_answer: int = field(default=0)
