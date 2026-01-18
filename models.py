def validate_task_structure(task):
    if not isinstance(task, dict):
        return False
    return all(key in task for key in ["id", "description", "completed"])


def get_next_id(tasks):
    if not tasks:
        return 1

    try:
        valid_ids = [
            task.get("id")
            for task in tasks
            if validate_task_structure(task) and isinstance(task.get("id"), int)
        ]

        if not valid_ids:
            return 1

        return max(valid_ids) + 1
    except (ValueError, TypeError):
        return 1


def find_task_by_id(tasks, task_id):
    for task in tasks:
        if validate_task_structure(task) and task.get("id") == task_id:
            return task
    return None
