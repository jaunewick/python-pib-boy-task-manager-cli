import os
import pickle
from datetime import datetime

tasks = []
TASK_FILE =  tasks.pkl

class TaskManager():
    def __init__(self, title, created_at, is_done=False):
        self.title = title
        self.created_at = created_at
        self.is_done = is_done

# Create
def add_task():
    title = input("Type your task: ")
    created_at = datetime.now().strftime("%d/%m %H:%M")

    task = TaskManager(title, created_at)
    tasks.append(task)
    # TODO Save to pickle file

# Read
def print_all_tasks():
    print("+------+-------------------------------------+--------------+--------+")
    print("|  ID  |            Task Title               |  Created at  |  Done  |")
    print("+------+-------------------------------------+--------------+--------+")
    for i, task in enumerate(tasks):
        print(f"| {i + 1:4} | {task.title:35} | {task.created_at:12} | {'✅' if task.is_completed else '❌':6} |")
    print("+------+-------------------------------------+--------------+--------+")

# Update
def update_task():
    print_all_tasks()

    id = int(input("Enter the ID of the task:"))

    tasks[id].is_done = True
    # TODO Save to pickle file




# Delete
