import os
import pickle
from datetime import datetime

tasks = []
TASK_FILE =  "tasks.pkl"

class TaskManager():
    def __init__(self, title, created_at, is_done=False):
        self.title = title
        self.created_at = created_at
        self.is_done = is_done

# Create
def add_task():
    print("|")
    title = input("+-- Type your task : ")
    created_at = datetime.now().strftime("%d/%m %H:%M")
    task = TaskManager(title, created_at)
    tasks.append(task)
    save_to_file()
    print(f"\n⏳ Saving {title}...\n")

# Read
def print_all_tasks():
    print("+------+-------------------------------------+--------------+--------+")
    print("|  ID  |            Task Title               |  Created at  |  Done  |")
    print("+------+-------------------------------------+--------------+--------+")
    for i, task in enumerate(tasks):
        print(f"| {i + 1:4} | {task.title:35} | {task.created_at:12} | {'✅' if task.is_done else '❌':6}|")
    print("+------+-------------------------------------+--------------+--------+")

# Update
def update_task():
    try:
        print("|")
        id = int(input("+-- Enter the ID of the task : ")) - 1
        tasks[id].is_done = True
        save_to_file()
        print(f"\n⏳ Updating {tasks[id].title}...\n")
    except IndexError:
        print("|")
        print("+-- Invalid ID. Try again...\n")
    except ValueError:
        print("|")
        print("+-- Invalid input. Try again...\n")

# Delete
def delete_task():
    try:
        print("|")
        id = int(input("+-- Enter the ID of the task : ")) - 1
        print(f"\n⏳ Deleting {tasks[id].title}...\n")
        del tasks[id]
        save_to_file()
    except IndexError:
        print("|")
        print("+-- Invalid ID. Try again...\n")
    except ValueError:
        print("|")
        print("+-- Invalid input. Try again...\n")

def print_cli_menu():
    while True:
        print("|")
        user_input = input("+-- Enter 'A' to add, 'U' to update to done, 'D' to delete, or 'Q' to quit : ").upper()
        match user_input:
            case 'A':
                add_task()
            case 'U':
                update_task()
            case 'D':
                delete_task()
            case 'Q':
                print("\n⏳ Shutting down Pip-Boy...\n")
                print("=== Thank you for using our software! ===\n")
                break
            case _:
                print("|")
                print("+-- Command not found. Try again...\n")
        print_all_tasks()

def already_existing_file():
    if os.path.exists(TASK_FILE):
        read_from_file()
        print_all_tasks()
    else:
        print("+=== Welcome to Pip-Boy Task Manager ===")
        add_task()
        print_all_tasks()

def save_to_file():
    # writing binary
    with open(TASK_FILE, "wb") as file:
        pickle.dump(tasks, file)

def read_from_file():
    global tasks
    if os.path.exists(TASK_FILE):
        # read binary
        with open(TASK_FILE, "rb") as file:
            tasks = pickle.load(file)


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    # Glowing green text
    print("\033[32;3m")
    already_existing_file()
    print_cli_menu()
