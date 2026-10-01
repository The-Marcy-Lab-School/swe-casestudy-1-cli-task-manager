"""Tests for start_app() in main.py."""

import main


def test_start_app_greets_runs_the_menu_and_says_goodbye(monkeypatch, capsys):
    # Replace the real menu so the test does not need to type any answers
    monkeypatch.setattr(main, 'show_menu', lambda: print('(menu runs here)'))

    main.start_app()

    assert capsys.readouterr().out == 'Welcome to the Task Manager!\n(menu runs here)\nGoodbye!\n'
