# Task Manager in Python (CLI)

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Version](https://img.shields.io/badge/version-3.1.0-blue)
![Python](https://img.shields.io/badge/python-3.10+-green)

Command-line interface (CLI) application developed in Python for task management.

This project was designed to practice solid programming fundamentals, clean code organization, and robust error handling in CLI applications.


---

## Features

* Unique, incremental, and reusable ID system
* Add, edit, complete, and remove tasks by ID
* Batch operations (add, remove, and complete multiple tasks)
* Task listing (all, completed, or pending)
* Automatic persistence using a JSON file
* Data validation when loading tasks
* Simple terminal-based interface
* Task creation and completion timestamps


---

## Running the Project

### Requirements

* Python 3.10 or higher
> This project uses Python 3.10+ due to structural pattern matching (`match/case`).

### How to run

```bash
python main.py
```

---

## Example usage

```text
#1 [✓] Buy milk
#5 [⏳] Study Python
#12 [⏳] Do exercises
```

IDs are permanent and only reused through the "Reorder tasks" operation.

---

## Technical Decisions

### Permanent IDs

Task IDs do not depend on the task's position in the list. They are always calculated based on the highest existing ID, avoiding common bugs caused by list indices and ensuring consistency after removals.

* Reordering is implemented to prevent continuous ID growth.

### JSON persistence

JSON was chosen for being simple, readable, and well-suited for a CLI application. When loading the file, only tasks with a valid structure are considered.

### Rollback on error

Whenever an operation changes the task state, the application immediately attempts to save the data. If saving fails, the previous in-memory state is restored, preventing inconsistencies between the task list and the file.

### Interactive batch operations

Batch operations allow multiple inputs in sequence, with individual validation and the option to stop at any time.

### Modularization

The codebase was modularized to separate responsibilities:

* `main.py`: application flow and user interface
* `tasks.py`: business logic
* `storage.py`: JSON file persistence
* `models.py`: validations and utilities

---

## Roadmap

* v1.0: Basic CLI with persistence
* v2.0: Unique ID system
* v2.1: Task filtering and editing
* v3.0: Batch operations
* v4.0: Desktop interface
* v5.0: Web version

---

## Technologies

* Python 3.10+
* JSON
* Git / GitHub

---

## Author

**Kauan Melo**
[GitHub](https://github.com/Sahvyt) • [LinkedIn](https://www.linkedin.com/in/kauan-melo-8b72a0305/)

---

## License

Open-source project for educational purposes.
