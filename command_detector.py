from commands import cat, cd, cp, echo, grep, ls, mkdir, mv, rm, touch


def detect_command(current_dir, user_input):
    command, *args = user_input.split()

    if command == "mkdir":
        directory_name = args[0]
        mkdir(current_dir, directory_name)
    elif command == "cd":
        directory_name = args[0]
        current_dir = cd(current_dir, directory_name)
    elif command == "ls":
        if args:
            specified_dir = args[0]
            specified_dir_obj = cd(current_dir, specified_dir)
            ls(specified_dir_obj)
            cd(specified_dir_obj, current_dir.name)
        else:
            ls(current_dir)
    elif command == "grep":
        if len(args) < 2:
            print("Error: Insufficient arguments for grep.")
            return current_dir
        file_name = args[0]
        pattern = args[1]
        if (pattern[0] == '"' and pattern[-1] == '"') or (
            pattern[0] == "'" and pattern[-1] == "'"
        ):
            pattern = pattern[1:-1]
            if file_name and pattern:
                grep(current_dir, file_name, pattern)
        else:
            print("Error: Type pattern in double or single quotes.")

    elif command == "touch":
        file_name = args[0]
        if file_name:
            touch(current_dir, file_name)
        else:
            print("Error: Insufficient arguments for touch.")
    elif command == "cat":
        file_name = args[0]
        if file_name:
            cat(current_dir, file_name)
        else:
            print("Error: Insufficient arguments for cat.")
    elif command == "echo":
        file_name = args[-1]
        mode = args[-2]
        content = " ".join(args[:-2])
        if (content[0] == '"' and content[-1] == '"') or (
            content[0] == "'" and content[-1] == "'"
        ):
            content = content[1:-1]
            if file_name:
                echo(current_dir, file_name, content, mode)
        else:
            print("Error: Insufficient arguments for echo.")
    elif command == "mv":
        source = args[0]
        destination = args[1]
        if source and destination:
            mv(current_dir, source, destination)
        else:
            print("Error: Insufficient arguments for mv.")
    elif command == "cp":
        source = args[0]
        destination = args[1]
        if source and destination:
            cp(current_dir, source, destination)
        else:
            print("Error: Insufficient arguments for cp.")
    elif command == "rm":
        target = args[0]
        if target:
            rm(current_dir, target)
    else:
        print("Error: Command not found.")
    return current_dir
