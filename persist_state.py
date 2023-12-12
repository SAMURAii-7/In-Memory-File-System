import json

from directory import Directory


def save_state(file_system, file_path):
    try:
        with open(file_path, "w") as file:
            json.dump(
                file_system,
                file,
                default=serialize_directory,
                indent=4,
            )
        print(f"File system state saved to '{file_path}'.")
    except Exception as e:
        print(f"Error: Unable to save file system state. {str(e)}")


def serialize_directory(directory):
    if isinstance(directory, Directory):
        serialized_dir = {
            "name": directory.name,
            "children": {
                name: serialize_directory(item)
                for name, item in directory.children.items()
            },
        }
        if directory.parent:
            serialized_dir["parent"] = directory.parent.name
        return serialized_dir
    elif isinstance(directory, str):
        return directory


def load_state(file_system, file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            file_system.children.clear()
            load_directory(file_system, data)
        print(f"File system state loaded from '{file_path}'.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Unable to decode JSON in '{file_path}'. {str(e)}")
    except Exception as e:
        print(f"Error: Unable to load file system state. {str(e)}")


def load_directory(directory, data):
    if isinstance(data, dict):
        for name, item_data in data.get("children", {}).items():
            if item_data is None:
                directory.children[name] = ""
            elif isinstance(item_data, (str, int, float, bool)):
                directory.children[name] = item_data
            elif isinstance(item_data, dict):
                new_directory = Directory(name)
                load_directory(new_directory, item_data)
                directory.children[name] = new_directory
    else:
        directory.children[data["name"]] = data["children"]
