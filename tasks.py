from models import get_next_id, find_task_by_id, validate_task_structure
from storage import save_tasks


def add_task(tasks):
    description = input("Task description: ").strip()

    if description == "":
        print("Description cannot be empty.")
        return

    task = {
        "id": get_next_id(tasks),
        "description": description,
        "completed": False
    }

    tasks.append(task)
    if save_tasks(tasks):
        print(f"Task #{task['id']} added successfully!")
    else:
        print(
            "Error: The task was added to the list, but could not be saved to the file."
        )
        tasks.remove(task)


def add_multiple_tasks(tasks):
    print("\nAdd multiple tasks (empty Enter to finish)")
    print("=" * 40)

    count = 0

    while True:
        description = input(f"Task {count + 1}: ").strip()

        if description == "":
            break

        task = {
            "id": get_next_id(tasks),
            "description": description,
            "completed": False
        }

        tasks.append(task)
        count += 1
        print(f"  → Task #{task['id']} added!")

    if count > 0:
        if save_tasks(tasks):
            print(f"\n{count} task(s) added successfully!")
        else:
            print(
                f"\nError: {count} task(s) were added to the list, but could not be saved."
            )
            for _ in range(count):
                tasks.pop()
    else:
        print("\nNo tasks were added.")


def list_tasks(tasks, filter_by=None):
    valid_tasks = [t for t in tasks if validate_task_structure(t)]
    filtered_tasks = valid_tasks

    if filter_by == "completed":
        filtered_tasks = [t for t in valid_tasks if t.get("completed", False)]
    elif filter_by == "pending":
        filtered_tasks = [t for t in valid_tasks if not t.get("completed", False)]

    if len(filtered_tasks) == 0:
        if filter_by == "completed":
            print("No completed tasks found.")
        elif filter_by == "pending":
            print("No pending tasks found.")
        else:
            print("No tasks found.")
        return

    for task in filtered_tasks:
        status = "✓" if task.get("completed", False) else "⏳"
        print(
            f"#{task.get('id', '?')} [{status}] {task.get('description', 'No description')}"
        )


def complete_task(tasks):
    if len(tasks) == 0:
        print("There are no tasks to complete.")
        return

    list_tasks(tasks)

    try:
        task_id = int(input("Enter the task ID to complete: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    task = find_task_by_id(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    if task.get("completed", False):
        print("This task is already completed.")
        return

    task["completed"] = True
    if save_tasks(tasks):
        print(f"Task #{task_id} marked as completed!")
    else:
        print(
            "Error: The task was marked as completed, but could not be saved."
        )
        task["completed"] = False


def complete_multiple_tasks(tasks):
    if len(tasks) == 0:
        print("There are no tasks to complete.")
        return

    print("\nComplete multiple tasks (empty Enter to finish)")
    print("=" * 40)
    list_tasks(tasks)
    print("=" * 40)

    count = 0
    completed_ids = []

    while True:
        entry = input(
            "Enter the task ID (or press Enter to finish): "
        ).strip()

        if entry == "":
            break

        try:
            task_id = int(entry)
        except ValueError:
            print("  → Invalid input. Please enter a number.")
            continue

        task = find_task_by_id(tasks, task_id)
        if not task:
            print(f"  → Task #{task_id} not found.")
            continue

        if task.get("completed", False):
            print(f"  → Task #{task_id} is already completed. Skipping...")
            continue

        task["completed"] = True
        completed_ids.append(task_id)
        count += 1
        print(f"  → Task #{task_id} marked as completed!")

    if count > 0:
        if save_tasks(tasks):
            print(f"\n{count} task(s) completed successfully!")
        else:
            print(
                f"\nError: {count} task(s) were completed, but could not be saved."
            )
            for task_id in completed_ids:
                task = find_task_by_id(tasks, task_id)
                if task:
                    task["completed"] = False
    else:
        print("\nNo tasks were completed.")


def remove_task(tasks):
    if len(tasks) == 0:
        print("There are no tasks to remove.")
        return

    list_tasks(tasks)

    try:
        task_id = int(input("Enter the task ID to remove: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    task = find_task_by_id(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    description = task.get("description", "")
    tasks.remove(task)
    if save_tasks(tasks):
        print(f"Task #{task_id} '{description}' removed successfully!")
    else:
        print(
            "Error: The task was removed from the list, but could not be saved."
        )
        tasks.append(task)
