from dataclasses import dataclass, field, fields
from typing import List

from code.data.SimpleWord import SimpleWord
from code.data.Translation import Translation

@dataclass
class Word(SimpleWord):
    skill: int = field(default=0)
    correct_answer: int = field(default=0)
    isRight: bool = field(default=None)
    answer: str = field(default="")
