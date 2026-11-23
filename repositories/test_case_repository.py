from models.test_case import TestCase

class TestCaseRepository:
    def __init__(self):
        self._test_cases: list[TestCase] = []
        self._next_id = 1

    def add(self, test_case: TestCase) -> TestCase:
        test_case.id = self._next_id
        self._test_cases.append(test_case)
        self._next_id += 1
        return test_case
    
    def get_all(self) -> list[TestCase]:
        return self._test_cases.copy()
 
