from dataclasses import dataclass
from models.steps import Step

@dataclass
class TestCase:
    id: int = 0
    test_case_id: str
    name: str
    purpose: str
    preconditions: str
    test_data: str
    steps: list[Step] = []
