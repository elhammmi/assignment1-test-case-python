import re, os
from utilities.console_color import ConsoleColor
def get_required_input(prompt: str) -> str:

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print(f"{ConsoleColor.RED}This field is required!{ConsoleColor.RESET}")

def check_test_case_id(prompt: str) -> str:

    while True:
        test_case_id = get_required_input(prompt).upper()

        if re.fullmatch(r"TC-[0-9]{3}", test_case_id):
            return test_case_id

        print(
            f"{ConsoleColor.RED}Invalid Test Case ID!"
            f"Use the format TC-001.{ConsoleColor.RESET}"
        )

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")