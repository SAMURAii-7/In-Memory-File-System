import json


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = {}
        self.parent = parent

    def add_child(self, child):
        self.children[child.name] = child


def mkdir(current_dir, name):
    new_directory = Directory(name, parent=current_dir)
    current_dir.add_child(new_directory)
    return new_directory


def get_last_child(current_dir, path):
    if path == "/":
        return path

    components = path.split("/")
    current = current_dir

    for component in components:
        if component == "":
            continue
        elif component == "..":
            current = getParent(current)
        else:
            if component in current.children and isinstance(
                current.children[component], Directory
            ):
                current = current.children[component]
            else:
                print(f"Error: Invalid path '{path}'")
                return -1
    return current


def get_full_path(current_dir):
    path_components = []

    while current_dir.name != "/":
        path_components.insert(0, current_dir.name)
        current_dir = getParent(current_dir)

    path_components.insert(0, "/")

    p = "/"
    return p + "/".join(path_components[1:])


def cd(current_dir, target_dir):
    if target_dir == "..":
        return getParent(current_dir)
    elif target_dir == "/" or target_dir == "~":
        root = getParent(current_dir)
        while root.name != "/":
            root = getParent(root)
        return root
    elif target_dir.count("/") >= 1:
        return get_last_child(current_dir, target_dir)
    elif target_dir in current_dir.children:
        if isinstance(current_dir.children[target_dir], Directory):
            return current_dir.children[target_dir]
        else:
            print(f"Error: '{target_dir}' is not a directory.")
    else:
        print(f"Error: Directory '{target_dir}' not found.")
        return current_dir


def getParent(current_dir):
    if current_dir.parent:
        return current_dir.parent
    else:
        # If current_dir is the root, return itself
        return current_dir


def ls(directory):
    path = get_full_path(directory)
    print(f"Contents of {path}:")
    for name, item in directory.children.items():
        if isinstance(item, Directory):
            print(f"  Directory: {name}")
        else:
            print(f"  File: {name}")


def touch(current_dir, file_name):
    if file_name in current_dir.children:
        print(f"Error: File '{file_name}' already exists.")
    else:
        current_dir.children[file_name] = ""
        print(f"File '{file_name}' created.")


def cat(current_dir, file_name):
    if file_name in current_dir.children and not isinstance(
        current_dir.children[file_name], Directory
    ):
        print(current_dir.children[file_name])
    else:
        print(f"Error: File '{file_name}' not found.")


def echo(current_dir, file_name, content, mode):
    if file_name in current_dir.children and not isinstance(
        current_dir.children[file_name], Directory
    ):
        if mode == ">":
            current_dir.children[file_name] = content
            print(f"Content written to '{file_name}'.")
        elif mode == ">>":
            current_dir.children[file_name] += "\n" + content
            print(f"Content appended to '{file_name}'.")
    else:
        print(f"Error: File '{file_name}' not found.")


def grep(current_dir, file_name, pattern):
    if file_name in current_dir.children and not isinstance(
        current_dir.children[file_name], Directory
    ):
        content = current_dir.children[file_name]
        lines = content.split("\n")
        matching_lines = [line for line in lines if pattern in line]
        if matching_lines:
            print("\n".join(matching_lines))
        else:
            print(f"Error: Pattern '{pattern}' not found in '{file_name}'.")
    else:
        print(f"Error: File '{file_name}' not found.")


def mv(current_dir, source, destination):
    if "/" not in source:
        source_dir = current_dir
        source_name = source
    else:
        if source.startswith("/"):
            if source.endswith("/"):
                parts = source[1:-1].split("/")
            else:
                parts = source[1:].split("/")
        else:
            parts = source.split("/")
        source_dir = get_last_child(current_dir, "/".join(parts[:-1]))
        if source_dir == -1:
            return
        source_name = parts[-1]
    if destination.startswith("/"):
        if destination.endswith("/"):
            destination_dir = get_last_child(current_dir, destination[1:-1])
        else:
            destination_dir = get_last_child(current_dir, destination[1:])
    else:
        destination_dir = get_last_child(current_dir, destination)
    if destination_dir == -1:
        return

    if source_name in source_dir.children:
        item = source_dir.children[source_name]
        del source_dir.children[source_name]
        destination_dir.children[source_name] = item
        print(f"Moved '{source}' to '{destination}'.")
    else:
        print(f"Error: Source '{source}' not found.")


# def cp(current_dir, source, destination):
#     if source in current_dir.children:
#         item = current_dir.children[source]
#         if isinstance(item, Directory):
#             # Copying a directory
#             new_directory = item.copy()
#             current_dir.children[destination] = new_directory
#             print(f"Copied directory '{source}' to '{destination}'.")
#         else:
#             # Copying a file
#             current_dir.children[destination] = item
#             print(f"Copied file '{source}' to '{destination}'.")
#     else:
#         print(f"Error: Source '{source}' not found.")


def cp(current_dir, source, destination):
    if "/" not in source:
        source_dir = current_dir
        source_name = source
    else:
        if source.startswith("/"):
            if source.endswith("/"):
                parts = source[1:-1].split("/")
            else:
                parts = source[1:].split("/")
        else:
            parts = source.split("/")
        source_dir = get_last_child(current_dir, "/".join(parts[:-1]))
        if source_dir == -1:
            return
        source_name = parts[-1]
    if destination.startswith("/"):
        if destination.endswith("/"):
            destination_dir = get_last_child(current_dir, destination[1:-1])
        else:
            destination_dir = get_last_child(current_dir, destination[1:])
    else:
        destination_dir = get_last_child(current_dir, destination)
    if destination_dir == -1:
        return

    if source_name in source_dir.children:
        item = source_dir.children[source_name]
        destination_dir.children[source_name] = item
        print(f"Copied '{source}' to '{destination}'.")
    else:
        print(f"Error: Source '{source}' not found.")


def rm(current_dir, target):
    if target in current_dir.children:
        del current_dir.children[target]
        print(f"Removed '{target}'.")
    else:
        print(f"Error: Target '{target}' not found.")


def save_state(file_system, file_path):
    try:
        with open(file_path, "w") as file:
            json.dump(
                file_system.copy().__dict__,
                file,
                default=lambda o: o.__dict__,
                indent=4,
            )
        print(f"File system state saved to '{file_path}'.")
    except Exception as e:
        print(f"Error: Unable to save file system state. {str(e)}")


def load_state(file_system, file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            # Clear existing file system
            file_system.children.clear()
            # Load the new file system structure
            load_directory(file_system, data)
        print(f"File system state loaded from '{file_path}'.")
    except Exception as e:
        print(f"Error: Unable to load file system state. {str(e)}")


def load_directory(directory, data):
    for name, item_data in data["children"].items():
        if item_data.get("children"):
            # If the item is a directory, recursively load its contents
            new_directory = Directory(name)
            load_directory(new_directory, item_data)
            directory.children[name] = new_directory
        else:
            # If the item is a file, simply add it
            directory.children[name] = item_data
