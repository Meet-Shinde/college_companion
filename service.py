#main logic
def add_task(tasks, title):
    tasks.append(title)

def list_task(tasks):
    if not tasks: #checks whether the lis is empty
        print("No tasks yet.")
        return
    print(f"\nTasks:")
    for i, tasks in enumerate(tasks, start=1):
        print(f"{i}] {tasks}")