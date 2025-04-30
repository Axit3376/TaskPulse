from emailer import send_email
from task_utils import get_due_soon_tasks


def format_tasks(tasks):
    if not tasks:
        return "No tasks due in the next 3 days."
    return "\n".join([f"- {t['title']} (Due: {t['due']})" for t in tasks])


def send_daily_reminder():
    tasks = get_due_soon_tasks()
    body = format_tasks(tasks)
    send_email("📅 Tasks Due Soon", body, "adityashekhar207@gmail.com")


if __name__ == "__main__":
    send_daily_reminder()
