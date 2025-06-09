from dataclasses import dataclass, field
from typing import List

from code.data.Word import Word


@dataclass
class Words:
    words:List[Word] = field(default_factory=list)

