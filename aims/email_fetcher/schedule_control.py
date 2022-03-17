from apscheduler.schedulers.background import BackgroundScheduler
import time
from pytz import timezone

#This method is for testing, we will be importing the run_backend from EmailBackend.py
def sendMessage():
    print('Yes')

sched = BackgroundScheduler(timezone="Asia/Singapore")
sched.start()

#Add jobs(Basically schedule when to run script)
job1 = sched.add_job(sendMessage,'cron',hour="15", minute="21") #(method,timertype,hour,minute)
job2 = sched.add_job(sendMessage,'cron',hour="15", minute="22")
job3 = sched.add_job(sendMessage,'cron',hour="15", minute="23")

#Just printing the job to see whether
print(job1)
print(job2)
print(job3)

#Add delay in the execution of a program
while True:
    time.sleep(1.0)