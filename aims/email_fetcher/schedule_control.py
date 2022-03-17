from apscheduler.schedulers.background import BackgroundScheduler
import time
from pytz import timezone

#This method is for testing, we will be importing the run_backend from EmailBackend.py
def sendMessage():
    print('yes')

sched = BackgroundScheduler(timezone="Asia/Singapore")
@sched.scheduled_job('interval', seconds=3)
def timed_job():
    print('This job is run every three seconds.')
sched.start()

#Add jobs(Basically schedule when to run script)
#job1 = sched.add_job(sendMessage,'cron',hour="16", minute="08") #(method,timertype,hour,minute)
#job2 = sched.add_job(sendMessage,'cron',hour="16", minute="02")
#job3 = sched.add_job(sendMessage,'cron',hour="16", minute="03")

#Just printing the job to see whether the job is created
#print(job1)
#print(job2)
#print(job3)

#Add delay in the execution of a program
#while True:
#    time.sleep(1.0)