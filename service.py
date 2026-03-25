#main logic
from datetime import datetime, timedelta
from db import(
    insert_task,
    get_all_tasks,
    complete_task_db,
    delete_task_db,
    get_tasks_due_between,
    get_all_tasks_sorted
)
import json
def add_task(title, due_date):
    datetime.strptime(due_date, "%Y-%m-%d") #validating
    created_at = datetime.now().strftime("%Y-%m-%d")
    insert_task(title, due_date, created_at)

def list_tasks():
    tasks=get_all_tasks()
    display_tasks(tasks)

def complete_task(task_id):
    return complete_task_db(task_id)

def delete_task(task_id):
    return delete_task_db(task_id)

def list_due_today():
    today=datetime.today().strftime("%Y-%m-%d")
    tasks=get_tasks_due_between(today, today)
    display_tasks(tasks)

def list_due_in_days(days):
    today=datetime.today()
    end_date=today+timedelta(days=days)
    tasks=get_tasks_due_between(
        today.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d"))
    display_tasks(tasks)

def list_tasks_sorted():
    tasks=get_all_tasks_sorted()
    display_tasks(tasks)

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

def display_tasks(tasks):
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