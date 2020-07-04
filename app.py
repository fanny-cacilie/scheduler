import schedule
import time

from helper import job, get_analysis_controller

# Time
schedule.every().seconds.do(job)
schedule.every(5).days.at("11:00").do(get_analysis_controller)

while True:
    schedule.run_pending()
    time.sleep(1)
