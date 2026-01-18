from storage import load_tasks, save_tasks
from tasks import (
    add_task,
    remove_task,
    complete_task,
    edit_task,
    list_tasks_menu,
    manage_tasks_menu,
)


def show_menu():
    print("\n" + "=" * 40)
    print("1 - Add task")
    print("2 - Remove task")
    print("3 - Complete task")
    print("4 - Edit task")
    print("5 - List tasks")
    print("6 - Manage multiple tasks")
    print("0 - Exit")
    print("=" * 40)


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        option = input("Choose an option: ")

        match option:
            case "1":
                add_task(tasks)
            case "2":
                remove_task(tasks)
            case "3":
                complete_task(tasks)
            case "4":
                edit_task(tasks)
            case "5":
                list_tasks_menu(tasks)
            case "6":
                manage_tasks_menu(tasks)
            case "0":
                if save_tasks(tasks):
                    print("Exiting...")
                else:
                    print("Warning: Unable to save changes before exiting.")
                    response = input("Do you want to exit anyway? (y/n): ").strip().lower()
                    if response == "y":
                        print("Exiting...")
                    else:
                        print("Operation cancelled. Changes have not been saved yet.")
                        continue
                break
            case _:
                print("Invalid option.")


if __name__ == "__main__":
    main()
