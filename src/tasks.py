"""Everything to do with the tasks themselves."""

# Tasks are stored in a list of dictionaries. We have provided some sample
# tasks so there is something on screen the first time you run the app.
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
    if not description:
        print("\nNo description provided.")
        return

    new_task = {
        "description": description,
        "is_complete": False,
    }
    tasks.append(new_task)
    print(f"\nTask \"{new_task['description']}\" added!")


def complete_task(task_index):
    # A negative index is valid in Python and counts from the end, so
    # tasks[-1] would quietly mark the LAST task complete. Check the lower
    # bound explicitly rather than relying on an error.
    if task_index < 0 or task_index >= len(tasks):
        print("\nInvalid task number.")
        return

    task = tasks[task_index]
    task["is_complete"] = True
    print(f"\nTask \"{task['description']}\" marked as completed!")


def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks yet! Add one to get started.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        # Prints out the task list like this:
        # 1. [x] Complete the CLI Task Manager project
        # 2. [ ] Answer investigation questions
        mark = "x" if task["is_complete"] else " "
        print(f"{index}. [{mark}] {task['description']}")
    print()


def clear_tasks():
    tasks.clear()
    print("\nAll tasks cleared!")
