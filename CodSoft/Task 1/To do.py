import argparse

tasks = []

def add_task(description, due_date, priority):
    task = {"description": description, "due_date": due_date, "priority": priority, "completed": False}
    tasks.append(task)

def list_tasks():
    for index, task in enumerate(tasks):
        print(f"{index+1}. {task['description']} (Due: {task['due_date']}, Priority: {task['priority']}, Completed: {task['completed']})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="To-Do List Application")
    parser.add_argument("action", choices=["add", "list"], help="Action to perform (add or list)")
    parser.add_argument("--description", help="Task description")
    parser.add_argument("--due_date", help="Due date")
    parser.add_argument("--priority", help="Priority")
    
    args = parser.parse_args()

    if args.action == "add":
        add_task(args.description, args.due_date, args.priority)
    elif args.action == "list":
        list_tasks()
