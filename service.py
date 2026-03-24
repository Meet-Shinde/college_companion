#main logic
from datetime import datetime, timedelta
from db import(
    insert_task,
    get_all_tasks,
    complete_task_db,
    delete_task_db
)
import json
def add_task(title, due_date):
    datetime.strptime(due_date, "%Y-%m-%d") #validating
    created_at = datetime.now().strftime("%Y-%m-%d")
    insert_task(title, due_date, created_at)

def list_tasks():
    tasks=get_all_tasks()
    if not tasks: #checks whether the list is empty
        print("No tasks yet.")
        return
    print(f"\nTasks:")
    for task in tasks:
        task_id, title, due_date, created_at, completed = task
        if completed:
            status="✓"
        else:
            status=" "
        print(f"{task_id}. {title} [{status}] \
(Due: {due_date}, Created: {created_at})")

def complete_task(task_id):
    return complete_task_db(task_id)

def delete_task(task_id):
    return delete_task_db(task_id)

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