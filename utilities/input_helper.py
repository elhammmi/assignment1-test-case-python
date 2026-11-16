import re, os

def get_required_input(prompt: str) -> str:

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("\033[91mError: This field is required!\033[0m")

def check_test_case_id(prompt: str) -> str:

    while True:
        test_case_id = get_required_input(prompt).upper()

        if re.fullmatch(r"TC-[0-9]{3}", test_case_id):
            return test_case_id

        print(
            "\033[91mInvalid Test Case ID! "
            "Use the format TC-001.\033[0m"
        )

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")