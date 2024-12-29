import os
import datetime

class ToDoListApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({
            'task': task,
            'status': 'Pending',
            'created_at': datetime.datetime.now()
        })
        print(f"Task added: {task}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = task['status']
                created_at = task['created_at'].strftime('%Y-%m-%d %H:%M:%S')
                print(f"{i}. [{status}] {task['task']} (Added on: {created_at})")

    def update_task(self, task_index):
        try:
            task_index = int(task_index) - 1
            if task_index < 0 or task_index >= len(self.tasks):
                print("Invalid task number.")
                return

            print("Choose the new status:")
            print("1. Pending\n2. Completed")
            choice = input("Enter your choice (1/2): ").strip()

            if choice == '1':
                self.tasks[task_index]['status'] = 'Pending'
                print("Task status updated to Pending.")
            elif choice == '2':
                self.tasks[task_index]['status'] = 'Completed'
                print("Task status updated to Completed.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    def delete_task(self, task_index):
        try:
            task_index = int(task_index) - 1
            if task_index < 0 or task_index >= len(self.tasks):
                print("Invalid task number.")
                return
            removed_task = self.tasks.pop(task_index)
            print(f"Task deleted: {removed_task['task']}")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        while True:
            print("\n==== To-Do List Menu ====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task Status")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                task = input("Enter the task description: ").strip()
                if task:
                    self.add_task(task)
                else:
                    print("Task description cannot be empty.")

            elif choice == '2':
                self.clear_screen()
                self.list_tasks()

            elif choice == '3':
                self.list_tasks()
                task_index = input("Enter the task number to update: ").strip()
                self.update_task(task_index)

            elif choice == '4':
                self.list_tasks()
                task_index = input("Enter the task number to delete: ").strip()
                self.delete_task(task_index)

            elif choice == '5':
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ToDoListApp()
    app.menu()
