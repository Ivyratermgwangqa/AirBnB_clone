# AirBnB Clone Project: Command Interpreter

## Overview

Welcome to the AirBnB clone project's initial stage! This project sets the groundwork for developing a comprehensive web application, guiding through fundamental concepts such as serialization, databases, unit testing, and command interpreters.

## Project Requirements

- **Python Version:** 3.8.5
- **Editors:** vi, vim, or emacs
- **Testing Framework:** `unittest`
- **File System:** Ubuntu 20.04 LTS
- **Code Style:** `pycodestyle` (version 2.8.*)
- **Documentation:** Comprehensive and clear documentation for all modules, classes, and functions.

## Execution

- Functional command interpreter in both interactive and non-interactive modes.
- All unit tests passing in both modes.

## Command Interpreter

The command interpreter is a crucial component that allows users to interact with the AirBnB application through a command-line interface. It provides functionality to create new objects, retrieve objects from various sources, perform operations on objects, update object attributes, and destroy objects.

### How to Start

To start the command interpreter, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Ivyratermgwangqa/AirBnB_clone.git
   ```

2. Navigate to the project directory:
   ```bash
   cd AirBnB_clone
   ```

3. Run the command interpreter:
   ```bash
   ./console.py
   ```

### How to Use

Once the command interpreter is running, you can use the following commands:

- **help:** Display a list of available commands and their descriptions.
- **EOF:** Exit the command interpreter.
- **quit:** Exit the command interpreter.

For detailed information on available commands, type `help <command>`.

## Execution

### Interactive Mode

To run the command interpreter in interactive mode, follow these steps:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-Interactive Mode

You can also use the command interpreter in non-interactive mode, similar to the Shell project in C. Here's how:

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Running Tests

All tests, including non-interactive mode tests, can be executed with the following command:

```bash
$ echo "python3 -m unittest discover tests" | bash
```

Make sure that all tests pass before finalizing your implementation.

## Authors

The following individuals have contributed to this repository:

- [Lerato Mgwangqa](https://github.com/Ivyratermgwangqa)
- [Kwizera Daniel](https://github.com/Dan2759)
