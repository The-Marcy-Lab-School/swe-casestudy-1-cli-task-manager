"""Shared setup for every test."""

import copy

import pytest

import tasks as tasks_module

# A snapshot of the sample tasks, taken once when the tests start
SAMPLE_TASKS = copy.deepcopy(tasks_module.tasks)


# autouse=True runs this fixture before every test without the test asking for it.
# The tasks list lives at module level, so a change made by one test would
# otherwise still be there in the next test.
@pytest.fixture(autouse=True)
def reset_tasks():
    # Replace the contents rather than the list itself, because the functions in
    # tasks.py refer to that same list object
    tasks_module.tasks[:] = copy.deepcopy(SAMPLE_TASKS)
