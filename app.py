from dialogs.test_case_dialog import TestCaseDialog
from repositories.test_case_repository import TestCaseRepository
from services.test_case_service import TestCaseService

repository = TestCaseRepository()
service = TestCaseService(repository)
dialog = TestCaseDialog(service)

def main():
    dialog.show_menu()

if __name__ == "__main__":
    main()