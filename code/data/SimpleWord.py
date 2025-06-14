from dataclasses import dataclass, field
from typing import List

from code.data.Translation import Translation


@dataclass
class SimpleWord:
    name: str = field(default="")
    transcription: str = field(default="")
    translations:List[Translation] = field(default_factory=list)
