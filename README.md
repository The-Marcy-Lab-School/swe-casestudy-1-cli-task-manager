# Project Overview

This project is a simple command-line task manager where users can add, view,
and complete tasks. The application stores tasks in a list of dictionaries,
gives users options through prompts, and uses iteration to handle interactions
with tasks.

## Key Features & Usage Example

After running the application, the user is presented with a menu of options.
They can:

1. Add a new task to their list of tasks
2. Mark a task as completed
3. Delete all tasks from the list
4. Exit the application

In the screenshot below, you can see a user selecting the "Add Task" option
and entering a task description "Return online order".

![A simple CLI task manager application.](img/task-manager-screenshot.png)

## Setup

Follow these steps to get started:

```sh
git clone git@github.com:The-Marcy-Lab-School/swe-casestudy-1-cli-task-manager.git
cd swe-casestudy-1-cli-task-manager

# Create a virtual environment in a folder named .venv, then turn it on
python3 -m venv .venv
source .venv/bin/activate

# Install pytest into the virtual environment
pip install pytest

# Run the application
python3 src/main.py
```

A virtual environment is a folder that holds its own copy of Python and the project's own installed packages, so the packages you install for this project do not affect any other project on your computer. The `source .venv/bin/activate` command turns the virtual environment on for the current terminal window only. When the virtual environment is on, your terminal prompt begins with `(.venv)`.

Each time you open a new terminal window to work on this project, run `source .venv/bin/activate` again from the project folder. To turn the virtual environment off, run `deactivate`.

The application itself needs no third-party packages, because Python reads a line of typed input with the built-in `input()` function. The only package you install is `pytest`, which runs the tests.

## Running Tests

With the virtual environment turned on, run this command from the project folder:

```sh
pytest
```

The `pytest` command finds the test files in the `tests` folder (set by `pytest.ini`) and runs every function whose name begins with `test_`. Those test files have full access to the functions in the `src` folder (also because of `pytest.ini`) and they ensure that they behave as desired.

Add `-v` to the command (`pytest -v`) to see the name of each test and whether it passed.

## Key Technologies & Packages

- Python 3
- `input()` and `print()` from the built-in functions
- The `os` module from the standard library
- `pytest`
