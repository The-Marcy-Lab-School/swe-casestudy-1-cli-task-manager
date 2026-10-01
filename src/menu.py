"""Displays the menu and handles the user's input."""

import os

from tasks import add_task, view_tasks, complete_task, clear_tasks

def show_menu():
    is_running = True
    while is_running:
        print('\nMenu:')
        print('1. Add Task')
        print('2. Complete Task')
        print('3. Clear All Tasks')
        print('4. Exit')

        view_tasks()

        menu_choice = input('\nChoose an option (1-4): ').strip()

        if menu_choice == '1':
            description = input('Enter task description: ').strip()
            add_task(description)
        elif menu_choice == '2':
            task_choice = input('Enter task number to complete: ').strip()
            try:
                task_index = int(task_choice) - 1
                complete_task(task_index)
            except ValueError:
                print(f'"{task_choice}" is not a number.')
        elif menu_choice == '3':
            clear_tasks()
        elif menu_choice == '4':
            is_running = False
        else:
            print('Invalid option. Please choose 1-4.')

        input('\nPress Enter to continue...')

        # Clear the output so that the "rounds" of messages don't pile up
        os.system('clear')