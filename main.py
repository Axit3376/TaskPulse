from task_utils import (
    create_task, view_tasks, delete_task,
    task_done, show_stats, edit_task,
    view_task_by_filter
)

from colorama import Fore, Style, init
init(autoreset=True)



def menu():
    print("Select your choice:")
    print("1. Add a Task")
    print("2. View all Tasks")
    print("3. Delete a Task")
    print("4. Mark Task as Done")
    print("5. Filter Tasks")
    print("6. Edit Task")
    print("7. Show Task Stats")
    print("8. Exit")


def main():
    while True:
        menu()
        try:
            user_choice = int(input("Enter your choice: "))
            if user_choice == 1:
                create_task()
            elif user_choice == 2:
                view_tasks()
            elif user_choice == 3:
                delete_task()
            elif user_choice == 4:
                task_done()
            elif user_choice == 5:
                view_task_by_filter()
            elif user_choice == 6:
                edit_task()
            elif user_choice == 7:
                show_stats()
            elif user_choice == 8:
                print("Exiting...")
                break
            else:
                print("Still working on other functionalities!\n")
        except ValueError:
            print("Please enter a valid number!\n")


if __name__ == '__main__':
    main()
