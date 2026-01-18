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
            "descr
