import json
from datetime import datetime

class Task:
    def __init__(self, title, description="", due_date=None, priority=0, status="Incomplete", category="Personal"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.category = category

    def update_status(self, new_status):
        self.status = new_status

    def update_category(self, new_category):
        self.category = new_category

    def __str__(self):
        return f"{self.title} ({self.status})"

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            tasks_data = json.load(f)
            return [Task(**task_data) for task_data in tasks_data]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    tasks_data = [task.__dict__ for task in tasks]
    with open("tasks.json", "w") as f:
        json.dump(tasks_data, f)

def display_menu():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Search Tasks")
    print("6. Filter Tasks")
    print("7. Save and Quit")
   # print("Enter your choice:")
    

def get_user_input(prompt):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description (optional): ")
    due_date_str = input("Enter due date (YYYY-MM-DD, optional): ")
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
    priority = int(input("Enter priority (0-10, optional): "))
    category = input("Enter category (optional): ")
    task = Task(title, description, due_date, priority, category=category)
    tasks.append(task)
    print("Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def mark_task_completed(tasks):
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index].update_status("Completed")
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted.")
    else:
        print("Invalid task number.")

def search_tasks(tasks, keyword):
    matching_tasks = [task for task in tasks if keyword.lower() in task.title.lower()]
    if matching_tasks:
        print("Search results:")
        for i, task in enumerate(matching_tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No matching tasks found.")

def filter_tasks(tasks, category):
    filtered_tasks = [task for task in tasks if task.category == category]
    if filtered_tasks:
        print("Filtered tasks:")
        for i, task in enumerate(filtered_tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the specified category.")

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = get_user_input("Enter your choice:")

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            mark_task_completed(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            keyword = input("Enter keyword to search: ")
            search_tasks(tasks, keyword)
        elif choice == 6:
            category = input("Enter category to filter: ")
            filter_tasks(tasks, category)
        elif choice == 7:
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break

if __name__ == "__main__":
    main()