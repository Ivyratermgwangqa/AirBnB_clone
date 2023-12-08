# Airbnb Clone Project

![Airbnb Logo](https://github.com/Dan2759/AirBnB_clone/assets/122816970/4b70d0e8-84fb-4dc1-8e6f-1616849b9450)

## Table of Contents
- [**Introduction**](#introduction)
- [**Getting Started**](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [**How to Use**](how-to-use)
- [**Command Line Interface**](#command-line-interface)
- [**Project Structure**](#project-structure)-
- [**Running Tests**](#running-rests)
- [**Contributing**](#contributing)
- [**Authors**](#authors)
- [**License**](#license)

## Introduction

Welcome to the AirBnB clone project's initial stage! This project sets the groundwork for developing a comprehensive web application, guiding through fundamental concepts such as serialization, databases, unit testing, and command interpreters.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:
- **Python Version:** 3.8.5
- **Editors:** vi, vim, or emacs
- **Testing Framework:** `unittest`
- **File System:** Ubuntu 20.04 LTS
- **Code Style:** `pycodestyle` (version 2.8.*)
- **Documentation:** Comprehensive and clear documentation for all modules, classes, and functions.


### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Dan2759/Airbnb_clone.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Airbnb-Clone
   ```

3. Run the command interpreter:
   
    ```bash
   ./console.py
   ```
    
## How to Use

Once the command interpreter is running, you can use the following commands:

- **help**: Display a list of available commands and their descriptions.
- **EOF**: Exit the command interpreter.
- **quit**: Exit the command interpreter.

For detailed information on available commands, type help <command>.

## Command Line Interface

We have a powerful Command Line Interface (CLI) to interact with the Airbnb Clone. Here are some examples:

- To create a new instance:

  ```bash
  ./console.py create BaseModel
  ```

- To show information about an instance:

  ```bash
  ./console.py show BaseModel instance_id
  ```

- To update an instance:

  ```bash
  ./console.py update BaseModel instance_id attribute_name "attribute_value"
  ```
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

## Project Structure

Describe the structure of your project. Here is a high-level overview:

```plaintext
Airbnb-Clone/
│
├── models/
│   ├── base_model.py
│   ├── user.py
│   └── ...
│
├── tests/
│   ├── test_console.py
│   └── ...
│
├── console.py
├── airbnb_manager.py
├── README.md
├── AUTHOURS
└── ...
```

## Running Tests

All tests, including non-interactive mode tests, can be executed with the following command:

```bash
$ echo "python3 -m unittest discover tests" | bash
```

Make sure that all tests pass before finalizing your implementation.

## Authors

The following individuals have contributed to this repository:

- [Lerato Mgwangqa](https://github.com/Ivyratermgwangqa)
- [Kwizera Daniel](https://github.com/Dan2759)

## License
