import os
import json
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            return json.load(file)
    else:
        return []
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
def show_tasks(tasks):
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")
def add_task(tasks, new_task):
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Added: {new_task}")
def mark_task_done(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks[task_index - 1]
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Marked as done: {task}")
    else:
        print("Invalid task index.")
def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks[task_index - 1]
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Deleted: {task}")
    else:
        print("Invalid task index.")
def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter a new task: ")
            add_task(tasks, new_task)
        elif choice == '3':
            task_index = int(input("Enter the task index to mark as done: "))
            mark_task_done(tasks, task_index)
        elif choice == '4':
            task_index = int(input("Enter the task index to delete: "))
            delete_task(tasks, task_index)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
