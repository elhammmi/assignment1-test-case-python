from repositories.test_case_repository import TestCaseRepository
from models.create_test_case_dto import CreateTestCaseDto
from models.create_test_case_result import CreateTestCaseResult
from models.get_test_case_result import GetTestCasesResult

class TestCaseService:
     _repository: TestCaseRepository


     def registerTestCase(test_case: CreateTestCaseDto) -> CreateTestCaseResult:
          pass
     
     def showTestCases() -> GetTestCasesResult:
          pass

