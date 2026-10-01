"""The main entry point for the application."""

from menu import show_menu


def start_app():
    print('Welcome to the Task Manager!')
    show_menu()
    print('Goodbye!')


if __name__ == "__main__":
    start_app()