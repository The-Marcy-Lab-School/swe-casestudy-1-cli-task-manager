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
git clone [repo_url]
cd [repo_name]
python3 src/main.py
```

There are no dependencies to install. Python reads a line of typed input with
the built-in `input()` function, so there is no package file and nothing to
download.

## Key Technologies & Packages

* Python 3
* No third-party packages

## Investigation

The questions in [INVESTIGATION.md](./INVESTIGATION.md) walk through how this
application is built and why. Work through them before building your own CLI
app.
