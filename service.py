#main logic
from datetime import datetime, timedelta
from db import(
    insert_task,
    get_all_tasks,
    complete_task_db,
    delete_task_db,
    get_tasks_due_between,
    get_all_tasks_sorted,
    insert_note,
    get_all_notes,
    delete_note_db,
    export_tasks_to_csv
)
def validate_task_title(title):
    if not title or not title.strip():
        raise ValueError("Task title cannot be empty.")

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d") #validating
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD format.")

def validate_note_content(content):
    if not content or not content.strip():
        raise ValueError("Note cannot be empty.")

def validate_id(value, name="ID"): #ID is the default value in funct.
    if value<=0:
        raise ValueError(f"{name} must be a positive number.")

def add_task(title, due_date):
    validate_task_title(title)
    validate_due_date(due_date)
    created_at = datetime.now().strftime("%Y-%m-%d")
    insert_task(title, due_date, created_at)

def get_all_tasks_data():
    tasks=get_all_tasks()
    return [task_row_to_dict(task) for task in tasks]

def complete_task(task_id):
    validate_id(task_id, "Task ID")
    return complete_task_db(task_id)

def delete_task(task_id):
    validate_id(task_id, "Task ID")
    return delete_task_db(task_id)

def get_tasks_due_today_data():
    today=datetime.today().strftime("%Y-%m-%d")
    tasks=get_tasks_due_between(today, today)
    return [task_row_to_dict(task) for task in tasks]

def get_tasks_due_in_days_data(days):
    today=datetime.today()
    end_date=today+timedelta(days=days)
    tasks=get_tasks_due_between(
        today.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d"))
    return [task_row_to_dict(task) for task in tasks]

def get_all_tasks_sorted_data():
    tasks=get_all_tasks_sorted()
    return [task_row_to_dict(task) for task in tasks]

def add_note(content):
    validate_note_content(content)
    created_at=datetime.now().strftime("%Y-%m-%d")
    insert_note(content, created_at)

def get_all_notes_data():
    notes=get_all_notes()
    return [note_row_to_dict(note) for note in notes]

def delete_note(note_id):
    validate_id(note_id, "Note ID")
    return delete_note_db(note_id)

def export_tasks():
    export_tasks_to_csv()

def task_row_to_dict(task):
    task_id, title, due_date, created_at, completed = task
    return {
        "id": task_id,
        "title": title,
        "due_date": due_date,
        "created_at": created_at,
        "completed": bool(completed)
    }

def note_row_to_dict(note):
    note_id, content, created_at = note
    return {
        "id": note_id,
        "content": content,
        "created_at": created_at
    }