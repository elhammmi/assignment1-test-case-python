from dialogs.test_case_dialog import TestCaseDialog
from repositories.test_case_repository import TestCaseRepository
from services.test_case_service import TestCaseService

test_case_repository = TestCaseRepository()
test_case_service = TestCaseService()
test_case_dialog = TestCaseDialog()
def main():
    test_case_dialog.show_menu()

if __name__ == "__main__":
    main()