# menu.py

from functions.iam_analyzer import analyze_iam_policies
from functions.aws_connector import get_iam_client
from functions.utils import display_menu_options, get_user_input

def main_menu():
    while True:
        display_menu_options()
        choice = get_user_input()

        if choice == '1':
            iam_client = get_iam_client()
            analyze_iam_policies(iam_client)
        elif choice == '2':
            # Implement other menu options here
            pass
        elif choice == '3':
            # Implement more menu options here
            pass
        elif choice == '4':
            # Implement even more menu options here
            pass
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
