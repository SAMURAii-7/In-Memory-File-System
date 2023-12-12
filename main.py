from file_system import Directory
from state_handler import execute_command
from command_detector import detect_command


def main():
    root = Directory(name="/")
    current_dir = root

    while True:
        user_input = input("fs> ")

        if user_input == "" or user_input.isspace():
            print("Error: No command provided.")
            continue

        if user_input.lower() == "exit":
            break

        # execute_command(current_dir, user_input)
        current_dir = detect_command(current_dir, user_input)


if __name__ == "__main__":
    main()
