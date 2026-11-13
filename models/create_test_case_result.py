from dataclasses import dataclass
from models.test_case import TestCase

@dataclass
class CreateTestCaseResult:
    succeeded: bool
    message: str
    errors: list[str]
    test_case_data: TestCase | None

