from directory import Directory
from utils import get_full_path


def ls(directory):
    path = get_full_path(directory)
    print(f"Contents of {path}:")

    sorted_items = sorted(directory.children.items(), key=lambda x: x[0].lower())

    for name, item in sorted_items:
        if isinstance(item, Directory):
            print(f"  {name}")
        else:
            print(f"  {name}")
