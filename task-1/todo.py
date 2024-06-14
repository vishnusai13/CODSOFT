# todo.py

tasks = []

def display_menu():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def update_task():
    view_tasks()
    if not tasks:
        return
    task_no = int(input("Enter the task number to update: "))
    if 1 <= task_no <= len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_no - 1] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    task_no = int(input("Enter the task number to delete: "))
    if 1 <= task_no <= len(tasks):
        tasks.pop(task_no - 1)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()