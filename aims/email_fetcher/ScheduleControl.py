from apscheduler.schedulers.background import BackgroundScheduler
import time
from pytz import timezone

def sendMessage():
    print('Yes')

sched = BackgroundScheduler(timezone="Asia/Singapore")
sched.start()
job1 = sched.add_job(sendMessage,'cron',hour="15", minute="21")
job2 = sched.add_job(sendMessage,'cron',hour="15", minute="22")
job3 = sched.add_job(sendMessage,'cron',hour="15", minute="23")
print(job1)
print(job2)
print(job3)
while True:
    time.sleep(1.0)