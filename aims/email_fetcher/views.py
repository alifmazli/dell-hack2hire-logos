from django.shortcuts import render
from .EmailBackend import EmailBackend
from apscheduler.schedulers.background import BackgroundScheduler

#Timer to schedule when to get attachment. Don't touch
sched = BackgroundScheduler(timezone="Asia/Singapore")
@sched.scheduled_job('cron',hour="08", minute="00", second='00')
def timed_job():
    print('Downloaded attachment')
    run = EmailBackend()
    run.run_email_backend()

@sched.scheduled_job('cron',hour="12", minute="00", second='00')
def timed_job():
    print('Downloaded attachment')
    run = EmailBackend()
    run.run_email_backend()

@sched.scheduled_job('cron',hour="18", minute="24", second='30')
def timed_job():
    print('Downloaded attachment')
    run = EmailBackend()
    run.run_email_backend()

sched.start()

"""
#For testing purposes, you can mess with this code
@sched.scheduled_job('interval', seconds=10)
def timed_job():
    print('Interval')
    run = EmailBackend()
    run.run_email_backend()
sched.start()
"""

#Views go here
def dashboard(request):
    return render(request, 'email_fetcher/index.html')
