#cli/menu
from service import add_task, list_task, complete_task
#connecting functions from service.py

def show_menu():
    print("\n=== College Companion ===")
    print("1] Add tasks")
    print("2] List tasks")
    print("3] Complete tasks")
    print("0] Exit Menu")

def main():
    tasks=[]
    while True:
        show_menu()
        choice=input("Enter your Choice: ").strip()
        if choice=="1":
            title=input("Add a task: ").strip()
            if title:
                add_task(tasks, title)
                print("Task added.")
            else:
                print("Task title cannot be empty.")
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
            except ValueError:
                print("Invalid Input. Enter a number.")
        elif choice=="0":
            print("Thank you for using this programe.\n")
            break
        else:
            print("Invalid Choice, Try again (1/2/3/0).")

#only run the main if the file is executed directly
if __name__=="__main__":
    main()