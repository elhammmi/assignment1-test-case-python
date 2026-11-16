from dataclasses import dataclass, field
from models.steps import Step

@dataclass
class TestCase:
    test_case_id: str
    name: str
    purpose: str
    preconditions: str
    test_data: str
    steps: list[Step] = field(default_factory=list)
    id: int = 0
