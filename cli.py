#cli/menu
from service import (
    add_task, 
    list_tasks, 
    complete_task,
    delete_task,
    list_due_today, 
    list_due_week,
    add_note,
    list_notes,
    save_notes,
    load_notes
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
    print("6] List tasks due in 7 days")
    print("7] Add notes")
    print("8] List notes")
    print("0] Exit Menu")

def main():
    create_tables()
    notes=load_notes()
    while True:
        show_menu()
        choice=input("Enter your Choice: ").strip()
        if choice=="1":
            title=input("Add a task: ").strip()
            due_date=input("Enter due date (YYYY-MM-DD): ").strip()
            if title and due_date:
                try:
                    add_task(title, due_date)
                    print("Task added.")
                except ValueError:
                    print("Invalid date format. Use YYYY-MM-DD.")
            else:
                print("Task title and due date cannot be empty.")
        elif choice=="2":
            list_tasks()
        elif choice=="3":
            try:
                task_id=int(input("Enter the ID to complete: "))
                success=complete_task(task_id)
                if success:
                    print("Task Completed.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid Input. Enter a number.")
        elif choice=="4":
            try:
                task_id=int(input("Enter the ID to complete: "))
                success=delete_task(task_id)
                if success:
                    print("Task Deleted.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid Input. Enter a number.")
        elif choice=="5":
            #list_due_today(tasks)
            print("This feature will be migrated to sqlite next.")
        elif choice=="6":
            #list_due_week(tasks)
            print("This feature will be migrated to sqlite next.")
        elif choice=="7":
            #addnote
            content=input("Add a note: ").strip()
            if content:
                add_note(notes, content)
                save_notes(notes)
                print("Note added.")
            else:
                print("Note cannot be empty.")
        elif choice=="8":
            list_notes(notes)
        elif choice=="0":
            print("Thank you for using this program.\n")
            break
        else:
            print("Invalid Choice, Try again (1/2/3/0).")

#only run the main if the file is executed directly
if __name__=="__main__":
    main()