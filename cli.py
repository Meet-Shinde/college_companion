#cli/menu
from service import (
    add_task, 
    complete_task,
    delete_task,
    get_all_tasks_data,
    get_tasks_due_today_data,
    get_tasks_due_in_days_data,
    get_all_tasks_sorted_data,
    add_note,
    delete_note,
    get_all_notes_data,
    export_tasks
)#connecting functions from service.py
from db import (
    create_tables,
)#connecting functions from db.py

def show_menu():
    print("\n=== College Companion ===")
    print("1] Add tasks")
    print("2] List tasks")
    print("3] Complete tasks")
    print("4] Delete tasks")
    print("5] List tasks due today")
    print("6] List tasks due in n days")
    print("7] List tasks sorted by due date.")
    print("8] Add notes")
    print("9] List notes")
    print("10] Delete notes")
    print("11] Export tasks to CSV")
    print("0] Exit Menu")

def main():
    create_tables()
    while True:
        show_menu()
        choice=input("Enter your Choice: ").strip()

        if choice=="1":
            title=input("Add a task: ").strip()
            due_date=input("Enter due date (YYYY-MM-DD): ").strip()
            try:
                add_task(title, due_date)
                print("Task added.")
            except ValueError as e:
                print(e)

        elif choice=="2":
            tasks=get_all_tasks_data()
            display_tasks(tasks)

        elif choice=="3":
            raw_id=input("Enter the ID to complete: ")
            try:
                task_id=int(raw_id)
            except ValueError:
                print("Invalid input. Enter a valid integer ID.")
                continue
            try:
                affected=complete_task(task_id)
                if affected:
                    print("Task Completed.")
                else:
                    print("Task not found.")
            except ValueError as e:
                print(e)

        elif choice=="4":
            raw_id=input("Enter the ID to delete: ")
            try:
                task_id=int(raw_id)
            except ValueError:
                print("Invalid input. Enter a valid integer ID.")
                continue
            try:
                affected=delete_task(task_id)
                if affected:
                    print("Task Deleted.")
                else:
                    print("Task not found.")
            except ValueError as e:
                print(e)

        elif choice=="5":
            tasks=get_tasks_due_today_data()
            display_tasks(tasks)

        elif choice=="6":
            try:
                days=int(input("Enter number of days: "))
                if days<0:
                    print("Enter a non-negative number.")
                else:
                    tasks=get_tasks_due_in_days_data(days)
                    display_tasks(tasks)
            except ValueError:
                print("Invalid input. Enter a number.")

        elif choice=="7":
            tasks=get_all_tasks_sorted_data()
            display_tasks(tasks)

        elif choice=="8":
            content=input("Add a note: ").strip()
            try:
                add_note(content)
                print("Note added.")
            except ValueError as e:
                print(e)

        elif choice=="9":
            notes=get_all_notes_data()
            display_notes(notes)

        elif choice=="10":
            raw_id=input("Enter the ID to delete: ")
            try:
                note_id=int(raw_id)
            except ValueError:
                print("Invalid input. Enter a valid integer ID.")
                continue
            try:
                affected = delete_note(note_id)
                if affected:
                    print("Note deleted.")
                else:
                    print("Note not found.")
            except ValueError as e:
                print(e)

        elif choice=="11":
            export_tasks()
            print("Tasks exported to tasks_export.csv file.")

        elif choice=="0":
            print("Thank you for using this program.\n")
            break
        else:
            print("Invalid Choice, Try again (1/2/3/0).")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nTasks:")
    for task in tasks:
        if task["completed"]:
            status="✓"
        else:
            status=" "
        print(f"{task["id"]}. {task["title"]} [{status}] \
        (Due: {task["due_date"]}, Created: {task["created_at"]})")

def display_notes(notes):
    if not notes:
        print("No notes saved.")
        return
    print("\nNotes: ")
    for note in notes:
        print(f"{note["id"]}. {note["content"]} (Created: {note["created_at"]})")

#only run the main if the file is executed directly
if __name__=="__main__":
    main()