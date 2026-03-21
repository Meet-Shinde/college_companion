#cli/menu
from service import (
    add_task, 
    list_task, 
    complete_task, 
    list_due_today, 
    list_due_week,
    save_tasks,
    load_tasks,
)
#connecting functions from service.py

def show_menu():
    print("\n=== College Companion ===")
    print("1] Add tasks")
    print("2] List tasks")
    print("3] Complete tasks")
    print("4] List tasks due today")
    print("5] List tasks due in 7 days")
    print("0] Exit Menu")

def main():
    tasks=load_tasks()
    while True:
        show_menu()
        choice=input("Enter your Choice: ").strip()
        if choice=="1":
            title=input("Add a task: ").strip()
            due_date=input("Enter due date (YYYY-MM-DD): ").strip()
            if title and due_date:
                add_task(tasks, title, due_date)
                print("Task added.")
            else:
                print("Task title and due date cannot be empty.")
            save_tasks(tasks)
        elif choice=="2":
            list_task(tasks)
        elif choice=="3":
            try:
                task_id=int(input("Enter the ID to complete: "))
                success=complete_task(tasks, task_id)
                if success:
                    print("Task Completed.")
                else:
                    print("Task not found.")
                save_tasks(tasks)
            except ValueError:
                print("Invalid Input. Enter a number.")
        elif choice=="4":
            list_due_today(tasks)
        elif choice=="5":
            list_due_week(tasks)
        elif choice=="0":
            print("Thank you for using this program.\n")
            break
        else:
            print("Invalid Choice, Try again (1/2/3/0).")

#only run the main if the file is executed directly
if __name__=="__main__":
    main()