from models.test_case import TestCase

class TestCaseRepository:
    _test_case : list[TestCase]
    _next_id: int

    def add(test_case: TestCase) -> TestCase:
        pass
    
    def getAll() -> list[TestCase]:
        pass
 
