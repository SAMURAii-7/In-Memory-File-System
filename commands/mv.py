from utils import get_last_child


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
