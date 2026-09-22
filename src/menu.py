"""Displays the menu and handles the user's input."""

from tasks import add_task, clear_tasks, complete_task, view_tasks


def clear_screen():
    # Two ANSI escape codes: move the cursor home, then clear the screen.
    print("\033[H\033[2J", end="")


def show_menu():
    is_running = True

    while is_running:
        print("Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Clear Tasks")
        print("4. Exit\n")

        view_tasks()

        menu_choice = input("Choose an option (1-4): ").strip()
        if menu_choice == "1":
            description = input("Enter task description: ")
            add_task(description)
        elif menu_choice == "2":
            task_choice = input("Enter task number to complete: ")
            # input() always gives a string, and int() raises if it is not a
            # number, so ask before converting.
            if task_choice.strip().lstrip("-").isdigit():
                complete_task(int(task_choice) - 1)
            else:
                print("\nInvalid task number.")
        elif menu_choice == "3":
            clear_tasks()
        elif menu_choice == "4":
            is_running = False
        else:
            print("Invalid option, try again.")

        input("\nPress Enter to continue...")
        clear_screen()
