import json
import os
from datetime import datetime

TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Add new task
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description (optional): ")
    due_date = input("Enter due date (YYYY-MM-DD, optional): ")

    task = {
        "id": int(datetime.now().timestamp()),
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")

# Show tasks
def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for idx, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "✘"
        print(f"{idx}. [{status}] {task['title']} (Due: {task.get('due_date', 'N/A')})")

# Mark task as completed
def mark_done():
    show_tasks()
    tasks = load_tasks()
    num = int(input("Enter task number to mark as done: "))
    if 0 < num <= len(tasks):
        tasks[num - 1]["completed"] = True
        save_tasks(tasks)
        print("✅ Task marked as completed!")
    else:
        print(" Invalid task number.")

# Delete a task
def delete_task():
    show_tasks()
    tasks = load_tasks()
    num = int(input("Enter task number to delete: "))
    if 0 < num <= len(tasks):
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f" Task '{removed['title']}' deleted!")
    else:
        print(" Invalid task number.")

# Main menu
def menu():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print(" Goodbye ")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
