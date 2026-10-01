"""Tests for the functions in tasks.py."""

from tasks import tasks, add_task, view_tasks, complete_task, clear_tasks

# capsys is a pytest "fixture" that captures everything printed during a test.
# capsys.readouterr().out returns that printed text as one string.


def test_sample_tasks_are_present_at_start():
    assert len(tasks) == 2
    assert tasks[0] == {"description": "Complete the CLI Task Manager project", "is_complete": True}
    assert tasks[1] == {"description": "Answer investigation questions", "is_complete": False}


def test_add_task_appends_an_incomplete_task():
    add_task('Buy groceries')

    assert len(tasks) == 3
    assert tasks[-1] == {"description": "Buy groceries", "is_complete": False}


def test_add_task_prints_a_confirmation(capsys):
    add_task('Buy groceries')

    assert capsys.readouterr().out == 'Task "Buy groceries" added!\n'


def test_add_task_refuses_an_empty_description(capsys):
    add_task('')

    assert len(tasks) == 2
    assert capsys.readouterr().out == 'Task description cannot be empty.\n'


def test_view_tasks_prints_numbered_tasks_with_checkboxes(capsys):
    view_tasks()

    assert capsys.readouterr().out == (
        '\nYour Tasks:\n'
        '1. [x] Complete the CLI Task Manager project\n'
        '2. [ ] Answer investigation questions\n'
    )


def test_view_tasks_prints_a_message_when_there_are_no_tasks(capsys):
    tasks.clear()

    view_tasks()

    assert capsys.readouterr().out == '\nNo tasks yet. Add one!\n'


def test_complete_task_marks_the_task_complete(capsys):
    complete_task(1)

    assert tasks[1]["is_complete"] is True
    assert capsys.readouterr().out == 'Task "Answer investigation questions" marked as completed!\n'


def test_complete_task_leaves_an_already_complete_task_complete():
    complete_task(0)

    assert tasks[0]["is_complete"] is True


def test_complete_task_rejects_an_index_past_the_end(capsys):
    complete_task(2)

    assert [task["is_complete"] for task in tasks] == [True, False]
    assert capsys.readouterr().out == 'Invalid task number.\n'


def test_complete_task_rejects_a_negative_index(capsys):
    # tasks[-1] is valid Python and means the last task, so without the
    # lower-bound check this would quietly complete "Answer investigation questions"
    complete_task(-1)

    assert tasks[1]["is_complete"] is False
    assert capsys.readouterr().out == 'Invalid task number.\n'


def test_clear_tasks_removes_every_task(capsys):
    clear_tasks()

    assert tasks == []
    assert capsys.readouterr().out == 'All tasks cleared!\n'
