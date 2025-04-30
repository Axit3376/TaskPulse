import json
import os


FILE_NAME = "tasks.json"


class Task:
    def __init__(self, title, due, priority, completed):
        self.title = title
        self.due = due
        self.priority = priority
        self.completed = completed


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            data = json.load(file)
            return data
    else:
        return []


def save_tasks(task_list):
    with open(FILE_NAME, 'w') as file:
        json.dump(task_list, file, indent=4)
