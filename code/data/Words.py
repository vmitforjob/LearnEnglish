from dataclasses import dataclass, field
from typing import List

from dataclasses_json import dataclass_json

from code.data.Word import Word

@dataclass_json
@dataclass(frozen=True)
class Words:
    words: List[Word] = field(default_factory=list)
