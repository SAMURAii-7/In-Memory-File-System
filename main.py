import os
from file_system import Directory
from state_handler import execute_command
from command_detector import detect_command

# Save state:
# py main.py -s "/filesystem.json"
# Load state:
# py main.py -l "/filesystem.json


def main():
    root = Directory(name="/")
    current_dir = root

    while True:
        user_input = input("fs> ")

        if user_input.lower() == "exit":
            break

        if user_input == "" or user_input.isspace():
            print("Error: No command provided.")
            continue

        if user_input.lower() == "clear":
            if os.name == "nt":
                os.system("cls")
            else:
                print("\033c", end="")
            continue

        # if user entered a single word command
        if user_input != "ls" and len(user_input.split()) == 1:
            print("Error: Invalid command.")
            continue

        # execute_command(current_dir, user_input)
        current_dir = detect_command(current_dir, user_input)


if __name__ == "__main__":
    main()
