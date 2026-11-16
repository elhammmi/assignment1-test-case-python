from repositories.test_case_repository import TestCaseRepository
from models.create_test_case_dto import CreateTestCaseDto
from models.create_test_case_result import CreateTestCaseResult
from models.get_test_case_result import GetTestCasesResult

class TestCaseService:

    def __init__(self, repository: TestCaseRepository):
        self._repository: TestCaseRepository = repository

    def register_test_case(self, test_case_dto: CreateTestCaseDto) -> CreateTestCaseResult:

        self._repository.add(test_case_dto)

    def get_test_cases(self) -> GetTestCasesResult:

        test_case_result = self._repository.get_all()
        return test_case_result


