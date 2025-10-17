# Initialize an empty list to store tasks
tasks = []

# Function to add a new task
def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f" '{task}' has been added successfully.\n")

# Function to display all tasks
def view_tasks():
    if not tasks:
        print(" No tasks available.\n")
        return
    print("\n Your To-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. {task['task']} [{status}]")
    print()

# Function to mark a task as completed
def mark_completed():
    view_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f" Task {task_num} marked as completed!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Function to delete a task
def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f" '{removed['task']}' has been deleted.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Function to display the main menu
def show_menu():
    print("========== TO-DO LIST MENU ==========")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")
    print("====================================")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.\n")
