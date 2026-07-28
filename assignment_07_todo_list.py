# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
# =============================================================================


def add_task(tasks):
    """Adds a new task to the list."""
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')


def view_tasks(tasks):
    """Displays all tasks."""
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")


def delete_task(tasks):
    """Deletes a task from the list."""
    if len(tasks) == 0:
        print("Your to-do list is empty.")
        return

    view_tasks(tasks)

    task_number = int(input("Enter task number to delete: "))

    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task}" has been removed.')
    else:
        print("Error: Invalid task number.")


def display_menu():
    """Displays the main menu."""
    print("\n============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 4.")


# Run the program
main()