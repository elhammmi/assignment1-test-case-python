from services.test_case_service import TestCaseService
from models.steps import Step
from models.create_test_case_dto import CreateTestCaseDto
import re

class TestCaseDialog:
    def __init__(self, _service: TestCaseService):
        self._service: TestCaseService = _service

    def addTestCase(self) -> None:
        print("")
        print("---Test Case Register---")
        print("")
        print("To register a new test case enter following instructions\n")

        #enter the testcase information
        test_case_id = input("Enter Test Case ID: ").strip()
        name = input("Enter Name: ").strip()
        purpose = input("Enter Purpose: ").strip()
        preconditions= input("Enter Preconditions: ").strip()
        test_case_data = input("Enter Test Data: ").strip()
        
        #enter the test case steps
        print("")
        print("To add the test case steps enter following information\n")

        steps= []
        step_number = 1

        while True:
            print(f"\nStep {step_number}")
            
            step_instruction = input(f"Enter the instruction: ").strip()
            step_expected_result= input(f"Enter the expected result: ").strip()
            step = Step(step_number, step_instruction, step_expected_result)
            steps.append(step)

            answer = input(
                "Add another step? (y/n): "
            ).strip().lower()

            if answer != "y":
                break

            step_number += 1

            request = CreateTestCaseDto(
            test_case_id=test_case_id,
            name=name,
            purpose=purpose,
            preconditions=preconditions,
            test_data= test_case_data,
            steps=steps
        )

        result = self._service.register_test_case(request)

        if result.succeeded:
            print("\nTest case registered successfully!")

            if result.test_case_data is not None:
                print(f"Test Case ID: {result.test_case_data.test_case_id} has registered with ID {result.test_case_data.id}")

            else:
                print("\nRegistration failed:")

            for error in result.errors:
                print(f"- {error}")



        
    def getTestCases() -> None:
          pass
     
    def show_menu(self) -> None:
        while True:
            print("\n--- Test Case Management ---")
            print("1. Register Test Case")
            print("2. Show All Test Cases")
            print("0. Exit")

            choice = input("Choose an option: ").strip()

            match choice:
                case "1":
                    self.addTestCase()

                case "2":
                    self.getTestCases()

                case "0":
                    print("Goodbye!")
                    break

                case _:
                    print("Invalid option. Please try again.")
