import json
import os
from models import validate_task_structure

FILE_PATH = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print(
                "Error: The tasks file does not contain a valid list. Creating a new one."
            )
            return []

        valid_tasks = [task for task in data if validate_task_structure(task)]
        invalid_tasks = len(data) - len(valid_tasks)

        if invalid_tasks > 0:
            print(
                f"Warning: {invalid_tasks} task(s) with an invalid structure were ignored."
            )

        return valid_tasks
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error while loading tasks: {e}")
        return []


def save_tasks(tasks):
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Error while saving tasks: {e}")
        return False
