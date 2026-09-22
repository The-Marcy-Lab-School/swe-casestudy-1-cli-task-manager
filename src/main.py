"""The main entry point for the application."""

from menu import clear_screen, show_menu


def start_app():
    clear_screen()
    print("Welcome to CLI Task Manager!\n")
    show_menu()
    print("Goodbye!")


if __name__ == "__main__":
    start_app()
