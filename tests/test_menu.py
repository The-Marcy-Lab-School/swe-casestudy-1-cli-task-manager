"""Tests for show_menu() in menu.py, which reads from input()."""

import pytest

from menu import show_menu
from tasks import tasks


# monkeypatch is a pytest fixture that temporarily replaces a function for one test.
# This fixture replaces input() with a function that returns the next prepared
# answer, so a test can play the part of the user.
@pytest.fixture
def type_answers(monkeypatch):
    # Without this, every round of the menu would really clear the terminal
    monkeypatch.setattr('os.system', lambda command: 0)

    def set_answers(*answers):
        remaining = list(answers)

        def fake_input(prompt=''):
            if not remaining:
                raise AssertionError(f'input() was called more times than expected, with the prompt {prompt!r}')
            return remaining.pop(0)

        monkeypatch.setattr('builtins.input', fake_input)

    return set_answers


# Every round of the menu ends with "Press Enter to continue...", which is the ''
# answer after each choice. Choosing '4' and pressing Enter exits the menu.


def test_choosing_exit_stops_the_menu(type_answers):
    type_answers('4', '')

    show_menu()

    assert len(tasks) == 2


def test_adding_a_task(type_answers, capsys):
    type_answers('1', 'Buy groceries', '', '4', '')

    show_menu()

    assert tasks[-1] == {"description": "Buy groceries", "is_complete": False}
    assert 'Task "Buy groceries" added!' in capsys.readouterr().out


def test_adding_a_task_strips_surrounding_spaces(type_answers):
    type_answers('1', '   Buy groceries   ', '', '4', '')

    show_menu()

    assert tasks[-1]["description"] == 'Buy groceries'


def test_adding_a_task_of_only_spaces_is_refused(type_answers, capsys):
    type_answers('1', '   ', '', '4', '')

    show_menu()

    assert len(tasks) == 2
    assert 'Task description cannot be empty.' in capsys.readouterr().out


def test_completing_a_task_by_its_displayed_number(type_answers):
    # The user sees the second task numbered 2, which is index 1 in the list
    type_answers('2', '2', '', '4', '')

    show_menu()

    assert tasks[1]["is_complete"] is True


def test_completing_a_task_with_a_non_number(type_answers, capsys):
    type_answers('2', 'abc', '', '4', '')

    show_menu()

    assert '"abc" is not a number.' in capsys.readouterr().out
    assert tasks[1]["is_complete"] is False


def test_completing_a_task_with_a_decimal_number(type_answers, capsys):
    type_answers('2', '1.5', '', '4', '')

    show_menu()

    assert '"1.5" is not a number.' in capsys.readouterr().out


def test_completing_task_zero_is_refused(type_answers, capsys):
    # Task 0 becomes index -1, which would mean the last task if it were not checked
    type_answers('2', '0', '', '4', '')

    show_menu()

    assert 'Invalid task number.' in capsys.readouterr().out
    assert tasks[1]["is_complete"] is False


def test_clearing_all_tasks(type_answers, capsys):
    type_answers('3', '', '4', '')

    show_menu()

    assert tasks == []
    assert 'All tasks cleared!' in capsys.readouterr().out


def test_an_unknown_option_shows_an_error_and_the_menu_repeats(type_answers, capsys):
    type_answers('7', '', '4', '')

    show_menu()

    output = capsys.readouterr().out
    assert 'Invalid option. Please choose 1-4.' in output
    assert output.count('Menu:') == 2


def test_the_menu_shows_the_options_and_the_task_list(type_answers, capsys):
    type_answers('4', '')

    show_menu()

    output = capsys.readouterr().out
    assert '1. Add Task' in output
    assert '2. Complete Task' in output
    assert '3. Clear All Tasks' in output
    assert '4. Exit' in output
    assert '2. [ ] Answer investigation questions' in output
