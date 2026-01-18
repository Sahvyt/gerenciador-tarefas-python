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
        "completed": False,
    }

    tasks.append(task)
    if save_tasks(tasks):
        print(f"Task #{task['id']} added successfully!")
    else:
        print("Error: The task was added to the list, but could not be saved.")
        tasks.remove(task)


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

    new_description = input("New description (or press Enter to cancel): ").strip()

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

    if filter_by == "completed":
        valid_tasks = [t for t in valid_tasks if t.get("completed")]
    elif filter_by == "pending":
        valid_tasks = [t for t in valid_tasks if not t.get("completed")]

    if not valid_tasks:
        print("No tasks found.")
        return

    for task in valid_tasks:
        status = "✓" if task.get("completed") else "⏳"
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
    if save_tasks(tasks):
        print("Task completed successfully!")
    else:
        print("Error saving task.")
        task["completed"] = False


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
        print("0 - Back")
        print("=" * 40)

        option = input("Choose an option: ")
        if option == "0":
            break
        else:
            print("Invalid option.")
