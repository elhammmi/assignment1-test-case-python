
from models.create_test_case_dto import CreateTestCaseDto
from models.steps import Step
from repositories.test_case_repository import TestCaseRepository as Repository
from services.test_case_service import TestCaseService as Service

def test_register_valid_test_case():
    # Arrange
    repository = Repository()
    service = Service(repository)

    dto = CreateTestCaseDto(
        test_case_id="TC-001",
        name="Login Test",
        purpose="Verify login functionality",
        preconditions="User is registered",
        test_data="Valid username and password",
        steps=[
            Step(
                id=1,
                instruction="Enter valid credentials",
                expected_result="User logs in successfully"
            )
        ]
    )

    # Act
    result = service.register_test_case(dto)

    # Assert
    assert result.succeeded is True
    assert result.errors == []
    assert result.test_case_data.test_case_id == "TC-001"
    assert result.test_case_data.id == 1


def test_register_test_case_with_invalid_id():
    # Arrange
    repository = Repository()
    service = Service(repository)

    dto = CreateTestCaseDto(
             test_case_id="test-001",
             name="Login Test",
             purpose="Verify login functionality",
             preconditions="User is registered",
             test_data="Valid username and password",
             steps=[
                 Step(
                     id=1,
                     instruction="Enter valid credentials",
                     expected_result="User logs in successfully"
                 )
             ]
         )

    #Act
    result = service.register_test_case(dto)
     
    # Assert
    assert result.succeeded is False
    assert len(result.errors) > 0
    assert result.test_case_data is None
    assert repository.get_all() == []

def test_get_all_registered_test_cases():
    # Arrange
    repository = Repository()
    service = Service(repository)

    for i in range(1, 3):
        dto = CreateTestCaseDto(
            test_case_id=f"TC-{i:03d}",
            name=f"Test Case {i}",
            purpose="Verify functionality",
            preconditions="User is registered",
            test_data="Valid test data",
            steps=[
                Step(
                    id=1,
                    instruction="Perform action",
                    expected_result="Action succeeds"
                )
            ]
        )

        service.register_test_case(dto)

    # Act
    result = service.get_test_cases()

    # Assert
    assert result.succeeded is True
    assert result.test_case_data is not None
    assert len(result.test_case_data) == 2
    assert result.test_case_data[0].test_case_id == "TC-001"
    assert result.test_case_data[1].test_case_id == "TC-002"


