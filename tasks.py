from models import get_next_id, find_task_by_id, validate_task_structure, get_current_timestamp
from storage import save_tasks


def add_task(tasks):
    description = input("Task description: ").strip()

    if description == "":
        print("Description cannot be empty.")
        return

    task = {
        "id": get_next_id(tasks),
        "description": description,
        "completed": False,
        "created_at": get_current_timestamp(),
        "completed_at": None
    }

    tasks.append(task)
    if save_tasks(tasks):
        print(f"Task #{task['id']} added successfully!")
    else:
        print("Error: The task was added to the list, but could not be saved.")
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
            "completed": False,
            "created_at": get_current_timestamp(),
            "completed_at": None
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


def edit_task(tasks):
    if not tasks:
        print("There are no tasks to edit.")
        return

    list_tasks(tasks)

    try:
        task_id = int(input("Enter the task ID to edit: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    task = find_task_by_id(tasks, task_id)
    if not task:
        print("Task not found.")
        return

    new_description = input(
        "New description (or press Enter to cancel): ").strip()

    if new_description == "":
        print("Edit cancelled.")
        return

    old_description = task["description"]
    task["description"] = new_description

    if save_tasks(tasks):
        print("Task updated successfully!")
    else:
        print("Error: Could not save changes.")
        task["description"] = old_description


def list_tasks(tasks, filter_by=None):
    valid_tasks = [t for t in tasks if validate_task_structure(t)]

    if not valid_tasks:
        print("No valid tasks found.")
        return

    filtered_tasks = valid_tasks

    if filter_by == "completed":
        filtered_tasks = [t for t in valid_tasks if t.get("completed", False)]
    elif filter_by == "pending":
        filtered_tasks = [
            t for t in valid_tasks if not t.get("completed", False)]

    if len(filtered_tasks) == 0:
        if filter_by == "completed":
            print("No completed tasks found")
        else:
            print("No pending tasks found.")
        return

    for task in filtered_tasks:
        status = "✓" if task.get("completed", False) else "⏳"
        print(f"#{task['id']} [{status}] {task['description']}")


def complete_task(tasks):
    if not tasks:
        print("There are no tasks to complete.")
        return

    list_tasks(tasks)

    try:
        task_id = int(input("Enter the task ID to complete: "))
    except ValueError:
        print("Invalid input.")
        return

    task = find_task_by_id(tasks, task_id)
    if not task:
        print("Task not found.")
        return

    if task["completed"]:
        print("Task already completed.")
        return

    task["completed"] = True
    task["completed_at"] = get_current_timestamp()

    if save_tasks(tasks):
        print("Task completed successfully!")
    else:
        print("Error saving task.")
        task["completed"] = False
        task["completed_at"] = None


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
        task["completed_at"] = get_current_timestamp()

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
                    task["completed_at"] = None
    else:
        print("\nNo tasks were completed.")


def remove_task(tasks):
    if not tasks:
        print("There are no tasks to remove.")
        return

    list_tasks(tasks)

    try:
        task_id = int(input("Enter the task ID to remove: "))
    except ValueError:
        print("Invalid input.")
        return

    task = find_task_by_id(tasks, task_id)
    if not task:
        print("Task not found.")
        return

    tasks.remove(task)
    if save_tasks(tasks):
        print("Task removed successfully!")
    else:
        print("Error saving changes.")
        tasks.append(task)


def remove_multiple_tasks(tasks):
    count = 0
    removed_ids = set()
    removed_tasks = []

    while True:
        entry = input(
            "Enter the task ID (or press Enter to finish): "
        ).strip()

        if entry == "":
            break

        try:
            task_id = int(entry)
        except ValueError:
            print("  → Invalid input. Please enter a number or press Enter to finish.")
            continue

        if task_id in removed_ids:
            print(
                f"  → Task #{task_id} has already been removed in this session. Skipping..."
            )
            continue

        task = find_task_by_id(tasks, task_id)

        if not task:
            print(f"  → Task #{task_id} not found. Try again.")
            continue

        tasks.remove(task)
        removed_ids.add(task_id)
        removed_tasks.append(task)
        count += 1

        print(f"  → Task #{task_id} removed!")

    if count > 0:
        if save_tasks(tasks):
            print(f"\n{count} task(s) removed successfully!")
        else:
            print(
                f"\nError: {count} task(s) were removed from the list, but could not be saved."
            )
            for task in removed_tasks:
                tasks.append(task)
    else:
        print("\nNo tasks were removed.")


def clean_completed_tasks(tasks):
    if len(tasks) == 0:
        print("There are no tasks to clean.")
        return

    print("\nClean completed tasks")
    print("=" * 40)

    list_tasks(tasks, filter_by="completed")
    print("=" * 40)

    response = input(
        "Do you want to remove all completed tasks? (y/n): "
    ).strip().lower()

    if response == "y":
        tasks_to_remove = [t for t in tasks if t.get("completed", False)]

        for task in tasks_to_remove:
            tasks.remove(task)

        if save_tasks(tasks):
            print("Completed tasks cleaned successfully!")
        else:
            print(
                "Error: Tasks were removed from the list, but could not be saved."
            )
            tasks.extend(tasks_to_remove)
    else:
        print("Operation cancelled.")


def reorder_tasks(tasks):
    if len(tasks) == 0:
        print("There are no tasks to reorder.")
        return

    print("\nReorder tasks")
    print("=" * 40)

    list_tasks(tasks)
    print("=" * 40)

    response = input(
        "Do you want to reorder all tasks? (y/n): "
    ).strip().lower()

    if response == "y":
        old_ids = []

        for i, task in enumerate(tasks, start=1):
            old_ids.append(task["id"])
            task["id"] = i

        if save_tasks(tasks):
            print("Tasks reordered successfully!")
        else:
            print(
                "Error: Tasks were reordered, but could not be saved."
            )
            for task, old_id in zip(tasks, old_ids):
                task["id"] = old_id
    else:
        print("Operation cancelled.")


def list_tasks_menu(tasks):
    while True:
        print("\n" + "=" * 40)
        print("LIST TASKS")
        print("1 - List all tasks")
        print("2 - List completed tasks")
        print("3 - List pending tasks")
        print("0 - Back")
        print("=" * 40)

        option = input("Choose an option: ")

        match option:
            case "1":
                list_tasks(tasks)
            case "2":
                list_tasks(tasks, "completed")
            case "3":
                list_tasks(tasks, "pending")
            case "0":
                break
            case _:
                print("Invalid option.")


def manage_tasks_menu(tasks):
    while True:
        print("\n" + "=" * 40)
        print("MANAGE TASKS")
        print("=" * 40)
        print("1 - Add multiple tasks")
        print("2 - Remove multiple tasks")
        print("3 - Complete multiple tasks")
        print("4 - Clear completed tasks")
        print("5 - Reorder tasks")
        print("0 - Back to main menu")
        print("=" * 40)

        option = input("Choose an option: ")

        match option:
            case "1":
                add_multiple_tasks(tasks)
            case "2":
                remove_multiple_tasks(tasks)
            case "3":
                complete_multiple_tasks(tasks)
            case "4":
                clean_completed_tasks(tasks)
            case "5":
                reorder_tasks(tasks)
            case "0":
                break
            case _:
                print("Invalid option.")
