from file_handler import load_tasks, save_tasks
from datetime import datetime, timedelta
from file_handler import load_tasks
from colorama import Fore, Style, init
init(autoreset=True)


def show_stats():
    task_list = load_tasks()
    total = len(task_list)
    completed = sum(1 for task in task_list if task['completed'])
    pending = total - completed

    print("\n📊 Task Stats:")
    print(f"Total Tasks     : {total}")
    print(f"Completed Tasks : {completed}")
    print(f"Pending Tasks   : {pending}\n")


def create_task():
    task = input(Fore.CYAN + "Enter the task: " + Fore.RESET)
    due = input(Fore.CYAN + "Enter the due date of the task: " + Fore.RESET)
    pri = int(input(Fore.CYAN + "Enter the priority (1=Low, 3=High): " + Fore.RESET))
    complete = False

    t = {
        "title": task,
        "due": due,
        "priority": pri,
        "completed": complete
    }
    task_list = load_tasks()
    task_list.append(t)
    save_tasks(task_list)

    print(Fore.GREEN + "✅ Task created successfully!\n")


def view_tasks():
    task_list = load_tasks()
    if not task_list:
        print(Fore.YELLOW + "⚠️ No tasks yet.\n" + Fore.RESET)
    else:
        for idx, task in enumerate(task_list, start=1):
            print(Fore.MAGENTA + f"{idx}. {task['title']} | Due: {task['due']} | Priority: {task['priority']}" + Fore.RESET)


def filter_by_completion():
    task_list = load_tasks()
    if not task_list:
        print(Fore.YELLOW + "⚠️ No tasks yet.\n" + Fore.RESET)
    else:
        for idx, task in enumerate(task_list, start=1):
            if task['completed']:
                print(Fore.GREEN + f"{idx}. {task['title']} (Completed)" + Fore.RESET)


def filter_by_due():
    task_list = load_tasks()
    if not task_list:
        print("No tasks yet.\n")
        return

    sorted_tasks = sorted(task_list, key=lambda x: x['due'])

    print("\n📅 Tasks sorted by due date:\n")
    for idx, task in enumerate(sorted_tasks, start=1):
        print(f"{idx}. {task['title']} | Due: {task['due']} | Priority: {task['priority']}")


def filter_by_priority():
    task_list = load_tasks()
    if not task_list:
        print("No tasks yet.\n")
        return

    sorted_tasks = sorted(task_list, key=lambda x: x['priority'], reverse=True)

    print("\n🔢 Tasks sorted by priority:\n")
    for idx, task in enumerate(sorted_tasks, start=1):
        print(f"{idx}. {task['title']} | Due: {task['due']} | Priority: {task['priority']}")


def view_task_by_filter():
    task_list = load_tasks()
    if not task_list:
        print("No tasks yet.\n")
    else:
        user_choice = int(input("Filter by tasks by: 1. Due | 2. Priority | 3. Completion | 4. Search by title "))
        if user_choice == 1:
            filter_by_due()
        elif user_choice == 2:
            filter_by_priority()
        elif user_choice == 3:
            filter_by_completion()
        elif user_choice == 4:
            search_task()
        else:
            print("Enter valid choice")


def delete_task():
    task_list = load_tasks()

    if not task_list:
        print(Fore.YELLOW + "⚠️ No tasks to delete.\n" + Fore.RESET)
        return

    print(Fore.MAGENTA + "Your current tasks:\n" + Fore.RESET)
    for idx, task in enumerate(task_list, start=1):
        print(f"{idx}. {task['title']} | Due: {task['due']} | Priority: {task['priority']}")

    try:
        choice = int(input(Fore.CYAN + "\nEnter the task number to delete: " + Fore.RESET))
        if 1 <= choice <= len(task_list):
            removed = task_list.pop(choice - 1)
            save_tasks(task_list)
            print(Fore.GREEN + f"\n✅ Deleted: {removed['title']}\n" + Fore.RESET)
        else:
            print(Fore.RED + "❌ Invalid task number.\n" + Fore.RESET)
    except ValueError:
        print(Fore.RED + "❌ Please enter a valid number.\n" + Fore.RESET)


def task_done():
    task_list = load_tasks()

    if not task_list:
        print(Fore.YELLOW + "⚠️ No tasks!\n" + Fore.RESET)
        return

    print(Fore.MAGENTA + "Your current tasks: \n" + Fore.RESET)
    for idx, task in enumerate(task_list, start=1):
        status = Fore.GREEN + "✔️" if task['completed'] else Fore.RED + "❌"
        print(f"{idx}. {task['title']} | Due: {task['due']} | Priority: {task['priority']} | Status: {status}")

    try:
        choice = int(input(Fore.CYAN + "\nEnter the task number to mark as done: " + Fore.RESET))
        if 1 <= choice <= len(task_list):
            completed_task = task_list[choice - 1]
            completed_task['completed'] = True
            save_tasks(task_list)
            print(Fore.GREEN + f"\n✅ Marked {completed_task['title']} as done!\n" + Fore.RESET)
        else:
            print(Fore.RED + "❌ Invalid task number.\n" + Fore.RESET)
    except ValueError:
        print(Fore.RED + "❌ Please enter a valid number.\n" + Fore.RESET)


def edit_task():
    task_list = load_tasks()

    if not task_list:
        print(Fore.YELLOW + "⚠️ No tasks to edit.\n" + Fore.RESET)
        return

    print(Fore.MAGENTA + "Your current tasks:\n" + Fore.RESET)
    for idx, task in enumerate(task_list, start=1):
        print(f"{idx}. {task['title']} | Due: {task['due']} | Priority: {task['priority']}")

    try:
        choice = int(input(Fore.CYAN + "\nEnter the task number to edit: " + Fore.RESET))
        if 1 <= choice <= len(task_list):
            selected = task_list[choice - 1]

            new_title = input(Fore.CYAN + f"Enter new title (leave blank to keep '{selected['title']}'): " + Fore.RESET)
            new_due = input(Fore.CYAN + f"Enter new due date (leave blank to keep '{selected['due']}'): " + Fore.RESET)
            new_priority_input = input(Fore.CYAN + f"Enter new priority (1-3) (leave blank to keep {selected['priority']}): " + Fore.RESET)

            if new_title:
                selected['title'] = new_title
            if new_due:
                selected['due'] = new_due
            if new_priority_input:
                try:
                    new_priority = int(new_priority_input)
                    if new_priority in [1, 2, 3]:
                        selected['priority'] = new_priority
                    else:
                        print(Fore.RED + "❌ Invalid priority. Keeping previous value." + Fore.RESET)
                except ValueError:
                    print(Fore.RED + "❌ Invalid input. Keeping previous priority." + Fore.RESET)

            save_tasks(task_list)
            print(Fore.GREEN + "\n✅ Task updated successfully!\n" + Fore.RESET)
        else:
            print(Fore.RED + "❌ Invalid task number.\n" + Fore.RESET)
    except ValueError:
        print(Fore.RED + "❌ Please enter a valid number.\n" + Fore.RESET)


def search_task():
    task_list = load_tasks()
    if not task_list:
        print("No tasks yet.\n")
        return

    keyword = input("Enter a keyword to search in task titles: ").strip().lower()

    matched_tasks = [task for task in task_list if keyword in task['title'].lower()]

    if not matched_tasks:
        print(f"No tasks found matching '{keyword}'.\n")
    else:
        print(f"\n🔍 Tasks matching '{keyword}':\n")
        for idx, task in enumerate(matched_tasks, start=1):
            print(f"{idx}. {task['title']} | Due: {task['due']} | Priority: {task['priority']}")


def get_due_soon_tasks():
    tasks = load_tasks()
    today = datetime.today()
    upcoming = []

    for task in tasks:
        try:
            due_date = datetime.strptime(task['due'], "%d/%m/%y")  # format: dd/mm/yy
            if 0 <= (due_date - today).days <= 3 and not task['completed']:
                upcoming.append(task)
        except ValueError:
            continue

    return upcoming
