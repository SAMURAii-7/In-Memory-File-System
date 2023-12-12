from directory import Directory
from utils import get_last_child, getParent


def cd(current_dir, target_dir):
    if target_dir == "..":
        return getParent(current_dir)
    elif target_dir == "/" or target_dir == "~":
        root = getParent(current_dir)
        while root and root.name != "/":
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
