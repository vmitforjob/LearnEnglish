from dataclasses import dataclass, field


@dataclass
class Translation:
    translation: str = field(default="")