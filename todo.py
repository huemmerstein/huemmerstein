import json
import os
import sys

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(description):
    tasks = load_tasks()
    task_id = max([t['id'] for t in tasks], default=0) + 1
    tasks.append({'id': task_id, 'description': description, 'done': False})
    save_tasks(tasks)
    print(f"Added task {task_id}: {description}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = '✓' if task['done'] else ' '
        print(f"{task['id']:3} [{status}] {task['description']}")


def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            save_tasks(tasks)
            print(f"Marked task {task_id} as done.")
            return
    print(f"Task {task_id} not found.")


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t['id'] != task_id]
    if len(tasks) == len(new_tasks):
        print(f"Task {task_id} not found.")
        return
    save_tasks(new_tasks)
    print(f"Deleted task {task_id}.")


def usage():
    print("Usage:")
    print("  python todo.py add 'task description'")
    print("  python todo.py list")
    print("  python todo.py done TASK_ID")
    print("  python todo.py delete TASK_ID")


def main():
    if len(sys.argv) < 2:
        usage()
        return

    command = sys.argv[1]
    if command == 'add' and len(sys.argv) >= 3:
        add_task(' '.join(sys.argv[2:]))
    elif command == 'list':
        list_tasks()
    elif command == 'done' and len(sys.argv) == 3:
        mark_done(int(sys.argv[2]))
    elif command == 'delete' and len(sys.argv) == 3:
        delete_task(int(sys.argv[2]))
    else:
        usage()


if __name__ == '__main__':
    main()
