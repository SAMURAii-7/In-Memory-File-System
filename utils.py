from directory import Directory


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
            if current is None:
                print(f"Error: Invalid path '{path}'")
                return -1
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
    while current_dir and current_dir.name != "/":
        path_components.insert(0, current_dir.name)
        current_dir = getParent(current_dir)

    path_components.insert(0, "/")

    p = "/"
    return p + "/".join(path_components[1:])


def getParent(current_dir):
    if current_dir.parent:
        return current_dir.parent
    else:
        return None
