#main logic
from datetime import datetime, timedelta
import json
def add_task(tasks, title, due_date):
    datetime.strptime(due_date, "%Y-%m-%d") #validating
    task_id=len(tasks)+1
    task={
        "id":task_id,
        "title":title,
        "done":False,
        "due_date": due_date,
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }
    tasks.append(task)
    #basically created a list of dictionaries

def list_tasks(tasks):
    if not tasks: #checks whether the list is empty
        print("No tasks yet.")
        return
    print(f"\nTasks:")
    for task in tasks:
        if task["done"]:
            status="✓"
        else:
            status=" "
        print(f"{task["id"]}. {task["title"]} [{status}] \
(Due: {task["due_date"]}, Created: {task["created_at"]})")

def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"]==task_id:
            task["done"]=True
            return True
    return False

def list_due_today(tasks):
    today=datetime.today().date()
    found=False
    print("\nTasks due today: ")
    for task in tasks:
        due=datetime.strptime(task["due_date"], "%Y-%m-%d").date()
        if due==today:
            if task["done"]:
                status="✓"
            else:
                status=" "
            print(f"{task["id"]}. {task["title"]} [{status}] \
(Due: {due})")
            found=True
    if not found:
        print("No tasks due today.")

def list_due_week(tasks):
    today=datetime.today().date()
    end_date=today+timedelta(days=7)
    found=False
    print("\nTasks due in the next seven days: ")
    for task in tasks:
        due=datetime.strptime(task["due_date"], "%Y-%m-%d").date()       
        if due==end_date:
            if task["done"]:
                status="✓"
            else:
                status=" "
            print(f"{task["id"]}. {task["title"]} [{status}] \
(Due: {due})")
            found=True
    if not found:
        print("No tasks due in next seven days.")

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_note(notes, content):
    note_id=len(notes)+1
    note={
        "id":note_id,
        "content":content,
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }
    notes.append(note)
    #again created a list of dictionaries

def list_notes(notes):
    if not notes:
        print("No notes saved.")
        return
    print("\nNotes: ")
    for note in notes:
        print(f"{note["id"]}. {note["content"]} (Created: {note["created_at"]})")

def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

def load_notes():
    try:
        with open("notes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []