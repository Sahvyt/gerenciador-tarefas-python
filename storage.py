import json
import os
from models import validate_task_structure, get_current_timestamp

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

        normalized_tasks = []
        ignored = 0

        for task in data:
            if not isinstance(task, dict):
                ignored += 1
                continue

            task.setdefault("completed", False)
            task.setdefault("created_at", get_current_timestamp())
            task.setdefault("completed_at", None)

            if validate_task_structure(task):
                normalized_tasks.append(task)
            else:
                ignored += 1

        if ignored > 0:
            print(
                f"Warning: {ignored} task(s) with invalid structure were ignored."
            )

        return normalized_tasks

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
