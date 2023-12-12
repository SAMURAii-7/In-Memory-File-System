from utils import get_last_child


def touch(current_dir, file_name):
    if file_name in current_dir.children:
        print(f"Error: File '{file_name}' already exists.")
    elif "/" in file_name:
        if file_name.startswith("/"):
            if file_name.endswith("/"):
                parts = file_name[1:-1].split("/")
            else:
                parts = file_name[1:].split("/")
        else:
            parts = file_name.split("/")
        destination_dir = get_last_child(current_dir, "/".join(parts[:-1]))
        if destination_dir == -1:
            return
        name = parts[-1]
        destination_dir.children[name] = ""
        print(f"File '{file_name}' created.")
    else:
        current_dir.children[file_name] = ""
        print(f"File '{file_name}' created.")
