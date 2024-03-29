# In-Memory File System in Python

## Introduction

This is a simple in-memory file system written in Python. It is a simplified version of the file system in Unix-like operating systems. It supports the following operations:

-   `mkdir`: create a new directory
-   `cd`: change the current working directory
-   `ls`: list the contents of a directory
-   `grep`: search for a string in a file
-   `cat`: print the contents of a file
-   `touch`: create a new file
-   `echo`: write/append text to a file
-   `mv`: move a file or directory
-   `cp`: copy a file or directory
-   `rm`: remove a file or directory

## Implementation

The core data structure is the `Directory` class, which models file system directories and holds a map of children (subdirectories or files). This class forms a `tree`-like structure where each directory has a reference to its parent, enabling easy navigation from child to parent. The get_absolute_path function efficiently traverses the file system to locate a specific directory based on an absolute path. I have implemented robust error handling for scenarios like invalid paths and insufficient command arguments. Notably, improvements include enhancing the `ls` command to display full item paths, refining the `cd` command to support both absolute and relative paths, and addressing formatting issues in commands like `echo`. I have also added the `grep` command which searches for a string in a file and prints the matching lines. The program supports saving the state of the file system to a JSON file and loading it back.

### It also supports storing the state of the file system in a JSON file and loading it back.

## Prerequisites

-   Python 3.x installed (tested on Python 3.10.4)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/SAMURAii-7/In-Memory-File-System.git
```

2. Navigate to the project directory:

```bash
cd in-memory-file-system
```

3. Run the program:

### Normal Mode

```bash
python main.py
```

### State Saving Mode

```bash
python main.py -s <json-file-path>
```

### State Loading Mode

-   This mode will load the state of the file system from the JSON file and then also automatically save the state of the file system to the same JSON file when the program exits.

```bash
python main.py -l <json-file-path>
```

## Usage

### `mkdir`

```bash
mkdir <directory_name>
```

### `cd`

```bash
cd <directory_name>
```

### `ls`

```bash
ls <directory_name>
```

### `grep`

```bash
grep <string> <file_name>
```

### `cat`

```bash
cat <file_name>
```

### `touch`

```bash
touch <file_name>
```

### `echo`

```bash
echo <text> > <file_name> # write text to file
echo <text> >> <file_name> # append text to file on a new line
```

### `mv`

```bash
mv <source> <destination>
```

### `cp`

```bash
cp <source> <destination>
```

### `rm`

```bash
rm <file_name>
rm <directory-name>
```
