from directory import Directory


def mkdir(current_dir, name):
    new_directory = Directory(name, parent=current_dir)
    current_dir.add_child(new_directory)
    return new_directory
