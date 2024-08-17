import os
import pickle
from datetime import datetime

tasks = []
TASK_FILE =  task.pkl

class TaskManager():
    def __init__(self, title, created_at, is_completed=False):
        self.title = title
        self.created_at = created_at
        self.is_completed = is_completed

# Create
def add_task():
    title = input("Type your task: ")
    created_at = datetime.now().strftime("%d/%m %H:%M")
    task = TaskManager(title, created_at)
    tasks.append(task)

    # TODO Save to pickle file

# Read

# Update

# Delete
