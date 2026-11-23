from repositories.test_case_repository import TestCaseRepository
from models.create_test_case_dto import CreateTestCaseDto
from models.create_test_case_result import CreateTestCaseResult
from models.get_test_case_result import GetTestCasesResult
from models.test_case import TestCase
import re

class TestCaseService:

    def __init__(self, repository: TestCaseRepository):
        self._repository: TestCaseRepository = repository

    def register_test_case(self, test_case_dto: CreateTestCaseDto) -> CreateTestCaseResult:
        
        errors = []

        if not test_case_dto:
            errors.append("Something went wrong")
            return CreateTestCaseResult(succeeded=False, message="The test case registration failed.",errors=errors,test_case_data=None)
        # Normalize Test Case ID
        test_case_id = test_case_dto.test_case_id.strip().upper()
        # Validate Test Case ID
        if not re.fullmatch(r"TC-[0-9]{3}", test_case_id):
            errors.append("Test Case ID must follow the format TC-001.")

        # Validate required fields
        if not test_case_dto.name.strip():
            errors.append("Name is required.")

        if not test_case_dto.purpose.strip():
            errors.append("Purpose is required.")

        if not test_case_dto.preconditions.strip():
            errors.append("Preconditions are required.")

        if not test_case_dto.test_data.strip():
            errors.append("Test data is required.")

        if not test_case_dto.steps:
            errors.append("At least one step is required.")

        # Validate steps
        for step in test_case_dto.steps:
            if not step.instruction.strip():
                errors.append(
                    f"Step {step.id}: Instruction is required."
                )

            if not step.expected_result.strip():
                errors.append(
                    f"Step {step.id}: Expected result is required."
                )

        # Return errors if validation fails
        if errors:
            return CreateTestCaseResult(
                succeeded=False,
                message="Test case registration failed.",
                errors=errors,
                test_case_data=None
            )

        # Convert DTO to TestCase
        test_case = TestCase(
            test_case_id=test_case_id,
            name=test_case_dto.name.strip(),
            purpose=test_case_dto.purpose.strip(),
            preconditions=test_case_dto.preconditions.strip(),
            test_data=test_case_dto.test_data.strip(),
            steps=test_case_dto.steps
        )



        self._repository.add(test_case)
        return CreateTestCaseResult(
            succeeded=True,
            message="Test case registered successfully.",
            errors=[],
            test_case_data=test_case
        )

    def get_test_cases(self) -> GetTestCasesResult:

        test_case_result = self._repository.get_all()
        return GetTestCasesResult(
            succeeded=True,
            message=None,
            errors=[],
            test_case_data=test_case_result
        )


