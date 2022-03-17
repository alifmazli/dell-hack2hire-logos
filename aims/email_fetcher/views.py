from django.shortcuts import render
from .EmailBackend import email_backend
from apscheduler.schedulers.background import BackgroundScheduler

#Timer to schedule when to get attachment. Don't touch
sched = BackgroundScheduler(timezone="Asia/Singapore")
@sched.scheduled_job('cron',hour="08", minute="00", second='00')
def timed_job():
    print('Downloaded attachment')
    run = email_backend.run_email_backend()

@sched.scheduled_job('cron',hour="12", minute="00", second='00')
def timed_job():
    print('Downloaded attachment')
    run = email_backend.run_email_backend()

@sched.scheduled_job('cron',hour="17", minute="00", second='00')
def timed_job():
    print('Downloaded attachment')
    run = email_backend.run_email_backend()
sched.start()

#For testing purposes, you can mess with this code
"""
@sched.scheduled_job('interval', second=10)
def timed_job():
    print('Downloaded attachment')
    run = email_backend.run_email_backend()
sched.start()
"""

#Views go here
def dashboard(request):
    return render(request, 'email_fetcher/index.html')
