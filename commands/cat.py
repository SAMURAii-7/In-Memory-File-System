from directory import Directory


def cat(current_dir, file_name):
    if file_name in current_dir.children and not isinstance(
        current_dir.children[file_name], Directory
    ):
        print(current_dir.children[file_name])
    else:
        print(f"Error: File '{file_name}' not found.")
