from services.test_case_service import TestCaseService
from models.steps import Step
from models.create_test_case_dto import CreateTestCaseDto


class TestCaseDialog:
    def __init__(self, _service: TestCaseService):
        self._service: TestCaseService = _service
    test_cases = []
    def add_test_case(self) -> None:
        print("")
        print("---Test Case Register---")
        print("")
        print("To register a new test case enter following instructions\n")

        while(True):
            
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

                step_answer = input(
                    "Add another step? (y/n): "
                ).strip().lower()

                if step_answer != "y":
                    break

                step_number += 1

            self.test_cases.append(self.test_cases)

            test_case_answer = input(
                "Add another test case? (y/n): "
                ).strip().lower()
            
            if test_case_answer != "y":
                    break

        request = CreateTestCaseDto(
            test_case_id=test_case_id,
            name=name,
            purpose=purpose,
            preconditions=preconditions,
            test_data= test_case_data,
            steps=steps
        )

        for test_case in self.test_cases:
            test_case = CreateTestCaseDto(
                        test_case_id=test_case_id,
                        name=name,
                        purpose=purpose,
                        preconditions=preconditions,
                        test_data= test_case_data,
                        steps=steps
                    )
            result = self._service.register_test_case(test_case)

            if result.test_case_data is not None:
                print(f"Test Case : {result.test_case_data.test_case_id} has successfully registered with ID {result.test_case_data.id}")

            else:
                print("\nRegistration failed:")

            for error in result.errors:
                print(f"- {error}")

        

        
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
            print(f"\n: {test_case.id}.")
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
            print("\n--- Test Case Management ---")
            print("1. Register Test Case")
            print("2. Show All Test Cases")
            print("0. Exit")

            choice = input("Choose an option: ").strip()

            match choice:
                case "1":
                    self.add_test_case()

                case "2":
                    self.get_test_cases()

                case "0":
                    print("Goodbye!")
                    break

                case _:
                    print("Invalid option. Please try again.")
