from django.shortcuts import render
from .EmailBackend import email_backend
from apscheduler.schedulers.background import BackgroundScheduler

#Timer to schedule when to get attachment. Don't disturb
sched = BackgroundScheduler(timezone="Asia/Singapore")
@sched.scheduled_job('interval', seconds=10)
def timed_job():
    print('Downloaded attachment')
    run = email_backend.run_email_backend()
sched.start()

#Views go here
def dashboard(request):
    return render(request, 'email_fetcher/index.html')
