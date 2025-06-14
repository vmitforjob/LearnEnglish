from dataclasses import dataclass, field
from typing import List

from dataclasses_json import dataclass_json

from code.data.VList import VList

@dataclass_json
@dataclass
class VLists:
    vLists:List[VList] = field(default_factory=list)

