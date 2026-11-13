from dataclasses import dataclass
from models.test_case import TestCase

@dataclass
class GetTestCasesResult:
    succeeded: bool
    message: str | None
    errors: list[str]
    test_case_data: list[TestCase] | None

