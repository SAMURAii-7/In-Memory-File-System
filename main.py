import argparse
import os
from file_system import Directory, load_state, save_state
from command_detector import detect_command


def main():
    root = Directory(name="/")
    current_dir = root

    parser = argparse.ArgumentParser(
        description="An in-memory file system built in python."
    )
    parser.add_argument(
        "-s", "--save", metavar="FILE", help="Save state to the specified file"
    )
    parser.add_argument(
        "-l", "--load", metavar="FILE", help="Load state from the specified file"
    )
    args = parser.parse_args()

    file_path = args.save or args.load

    if args.load:
        load_state(root, file_path)
        print(f"Loading state from {file_path}")

    while True:
        user_input = input("fs> ")

        if user_input.lower() == "exit":
            if args.save or args.load:
                save_state(root, file_path)
                print(f"Saving state to {file_path}")
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

        if user_input != "ls" and len(user_input.split()) == 1:
            print("Error: Invalid command.")
            continue

        current_dir = detect_command(current_dir, user_input)


if __name__ == "__main__":
    main()
