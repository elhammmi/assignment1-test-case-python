from models.test_case import TestCase

class TestCaseRepository:
    def __init__(self):
        self._test_cases = list[TestCase]
        self._next_id=0

    def add(self, test_case: TestCase) -> TestCase:
        self._test_cases.append(test_case)
    
    def get_all(self) -> list[TestCase]:
        return self._test_cases.copy()
 
