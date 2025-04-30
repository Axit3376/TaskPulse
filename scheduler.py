import schedule
import time
from daily_reminder import send_daily_reminder  # Import the function that sends emails


def job():
    send_daily_reminder()
    print("Running daily reminder...")


# Schedule the task at 9:00 AM every day
schedule.every().day.at("18:04").do(job)

# Infinite loop to keep the script running and check the schedule
while True:
    schedule.run_pending()  # Run any scheduled tasks
    time.sleep(15)  # Wait for 1 minute before checking again
