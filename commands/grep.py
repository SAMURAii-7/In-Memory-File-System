from directory import Directory


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
