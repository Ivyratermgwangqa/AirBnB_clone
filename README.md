# Airbnb Clone Project

![Airbnb Logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231208%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231208T000102Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e447e52d30aab50f979cbf026b1dd09338f95a81c834d35cf27168e2fe6784df)

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Command Line Interface](#command-line-interface)
- [Project Structure](#project-structure)
- [Running Tests](#Running Tests)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

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

3. Install dependencies

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

(insert_more_cli_commands_here)

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
├── setup_database.py
├── README.md
├── requirements.txt
└── ...
```

(insert_more_project_structure_here)


```

Replace the placeholder texts like `insert_logo_url_here` and others with the actual URLs and details of your project. Customize the sections according to your project's specifics.

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
