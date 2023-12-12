from directory import Directory


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
