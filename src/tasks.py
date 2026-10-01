"""Everything to do with the tasks themselves."""

# The list of tasks. Each task is a dictionary with a description and a completion flag.
# We have provided some sample tasks so there is something on screen the first time you run the app.
tasks = [
    {
        "description": "Complete the CLI Task Manager project",
        "is_complete": True,
    },
    {
        "description": "Answer investigation questions",
        "is_complete": False,
    },
]


def add_task(description):
    # A guard clause: refuse an empty description
    if not description:
        print('Task description cannot be empty.')
        return

    task = {"description": description, "is_complete": False}
    tasks.append(task)
    
    print(f'Task "{description}" added!')


# Prints out the task list like this:
# Your Tasks:
# 1. [x] Complete the CLI Task Manager project
# 2. [ ] Answer investigation questions
def view_tasks():
    if len(tasks) == 0:
        print('\nNo tasks yet. Add one!')
        return

    print('\nYour Tasks:')
    for index, task in enumerate(tasks, start=1):
        checkbox = '[x]' if task["is_complete"] else '[ ]'
        print(f'{index}. {checkbox} {task["description"]}')


def complete_task(task_index):
    if task_index < 0 or task_index >= len(tasks):
        print('Invalid task number.')
        return

    task = tasks[task_index]
    task["is_complete"] = True
    print(f'Task "{task["description"]}" marked as completed!')


def clear_tasks():
    tasks.clear()
    print('All tasks cleared!')