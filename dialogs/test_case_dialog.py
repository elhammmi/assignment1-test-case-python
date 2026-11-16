from services.test_case_service import TestCaseService
from models.steps import Step
from models.create_test_case_dto import CreateTestCaseDto
from utilities.input_helper import get_required_input, check_test_case_id, clear_screen


class TestCaseDialog:
    def __init__(self, _service: TestCaseService):
        self._service: TestCaseService = _service

    def add_test_case(self) -> None:
        print("")
        print("---Test Case Register---")
        print("")
        print("To register a new test case enter following instructions\n")

        while(True):
            
            #enter the testcase information
            test_case_id = check_test_case_id("Enter Test Case ID: ").strip()
            
            name = get_required_input("Enter Name: ").strip()
            purpose = get_required_input("Enter Purpose: ").strip()
            preconditions= get_required_input("Enter Preconditions: ").strip()
            test_case_data = get_required_input("Enter Test Data: ").strip()

            #enter the test case steps
            print("")
            print("To add the test case steps enter following information\n")

            steps= []
            step_number = 1

            while True:
                print(f"\nStep {step_number}")

                step_instruction = get_required_input(f"Enter the instruction: ").strip()
                step_expected_result= get_required_input(f"Enter the expected result: ").strip()
                step = Step(step_number, step_instruction, step_expected_result)
                steps.append(step)

                step_answer = input(
                    "Add another step? (y/n): "
                ).strip().lower()

                if step_answer != "y":
                    break

                step_number += 1

            # Create DTO for the current test case
            request = CreateTestCaseDto(
            test_case_id=test_case_id,
            name=name,
            purpose=purpose,
            preconditions=preconditions,
            test_data=test_case_data,
            steps=steps
            )

            # Register the current test case
            result = self._service.register_test_case(request)

            if result.succeeded and result.test_case_data is not None:
                print(
                    f"\nTest Case: {result.test_case_data.test_case_id} "
                    f"has successfully registered with ID "
                    f"{result.test_case_data.id}"
                 )
            else:
                print("\nRegistration failed:")

            # Ask whether to register another test case
            test_case_answer = input(
                "\nAdd another test case? (y/n): "
                ).strip().lower()
            if test_case_answer != "y":
                break
        
    def get_test_cases(self) -> None:
          
        print("\n--- Registered Test Cases ---")

        result = self._service.get_test_cases()

        if not result.succeeded:
            print(result.message or "Failed to retrieve test cases.")

            for error in result.errors:
                print(f"- {error}")

            return
        test_cases = result.test_case_data

        if not test_cases:
            print("No test cases registered.")
            return
        
        for test_case in test_cases:
            print(f"\n {test_case.id}.")
            print(f"Test Case ID: {test_case.test_case_id}")
            print(f"Name: {test_case.name}")
            print(f"Purpose: {test_case.purpose}")
            print(f"Preconditions: {test_case.preconditions}")
            print(f"Test Data: {test_case.test_data}")
            print("Steps:")
            for step in test_case.steps:
                print(f"  Step {step.id}: {step.instruction}")
                print(f"  Expected Result: {step.expected_result}")
            


     
    def show_menu(self) -> None:
        while True:
            clear_screen()
            print("\n--- Test Case Management ---")
            print("1. Register Test Case")
            print("2. Show All Test Cases")
            print("0. Exit")

            choice = input("Choose an option: ").strip()

            match choice:
                case "1":
                    clear_screen()
                    self.add_test_case()
                    input("\nPress Enter to return to the main menu...")

                case "2":
                    clear_screen()
                    self.get_test_cases()
                    input("\nPress Enter to return to the main menu...")

                case "0":
                    print("Goodbye!")
                    break

                case _:
                    clear_screen()
                    print("Invalid option. Please try again.")
                    input("\nPress Enter to continue...")
