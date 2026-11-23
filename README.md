# Test Case Register

A simple Python console application for registering and viewing software test cases. Test cases are stored in memory, so they are lost when the application closes.

## Features

- Register a test case with a Test Case ID, name, purpose, preconditions, test data, and one or more steps.
- Add instructions and expected results for each step.
- Validate required fields and Test Case IDs in the format `TC-001`.
- Automatically assign an internal numeric ID to each registered test case.
- Display all registered test cases and their steps.
- Use the menu until choosing **Exit**.

## Requirements

- Python 3.10 or later.
- `pytest` to run the unit tests.

## How to Run

Open a terminal in the project folder and run:

```bash
python app.py
```

Choose an option from the menu:

```text
1. Register Test Case
2. Show All Test Cases
0. Exit
```

The application does not require a database or any external packages to run.

## Project Structure

- `app.py` — creates the Repository, Service, and Dialog, then starts the menu.
- `models/` — defines `TestCase`, `Step`, the registration DTO, and result objects.
- `dialogs/` — handles the console menu, user input, and output.
- `services/` — validates test case data and handles registration and retrieval.
- `repositories/` — stores test cases in memory and assigns internal IDs.
- `utilities/` — provides input validation, console clearing, and output colors.
- `tests/` — contains unit tests for the application logic.

## Running Unit Tests

Install pytest:

```bash
python -m pip install pytest
```

Run the tests from the project root:

```bash
python -m pytest tests/ -v
```

## Design Reflection

I based the implementation on my UML diagrams. The diagrams are available in a separate GitHub repository: https://github.com/elhammmi/assignment1-diagrams. The class diagram defines the main components and their relationships, while the activity and sequence diagrams describe the registration and retrieval workflows.

I separated the application into Models, Dialog, Service, Repository, and Utilities to give each component a clear responsibility. The Dialog handles user interaction, the Service handles validation and application logic, and the Repository manages in-memory storage. `CreateTestCaseDto` carries registration data to the Service, and result objects return the outcome of operations.

## Limitations

- Data is not saved after the program exits.
- Test cases cannot be edited, deleted, or executed.
- The application does not check whether a Test Case ID has already been registered.
