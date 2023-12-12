def rm(current_dir, target):
    if target in current_dir.children:
        del current_dir.children[target]
        print(f"Removed '{target}'.")
    else:
        print(f"Error: Target '{target}' not found.")
