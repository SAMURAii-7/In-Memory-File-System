import json
from file_system import (
    load_state,
    save_state,
)


def parse_command(command):
    try:
        return json.loads(command.replace("'", '"'))
    except json.JSONDecodeError:
        raise ValueError("Invalid command format. Use valid JSON.")


def execute_command(file_system, command):
    parsed_command = parse_command(command)

    if "save_state" in parsed_command and parsed_command["save_state"] == "true":
        save_state(file_system, parsed_command["path"])
        print("File system state saved successfully.")
    elif "load_state" in parsed_command and parsed_command["load_state"] == "true":
        load_state(file_system, parsed_command["path"])
        print("File system state loaded successfully.")
    else:
        print("Error: Unrecognized command.")
