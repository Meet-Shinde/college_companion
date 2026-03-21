#main logic
def add_task(tasks, title):
    task_id=len(tasks)+1
    task={
        "id":task_id,
        "title":title,
        "done":False
    }
    tasks.append(task)
    #basically created a list of dictionaries

def list_task(tasks):
    if not tasks: #checks whether the lis is empty
        print("No tasks yet.")
        return
    print(f"\nTasks:")
    for i, task in enumerate(tasks, start=1):
        if task["done"]:
            status="✓"
        else:
            status=" "
        print(f"{task["id"]}. {task["title"]} [{status}]")

def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"]==task_id:
            task["done"]=True
            return True
    return False