from dataclasses import dataclass, field


@dataclass
class VList:
    name: str = field(default="")
    number: int = field(default=0)
    numberLearned: int = field(default=0)
    pathListWords: str = field(default="/")
