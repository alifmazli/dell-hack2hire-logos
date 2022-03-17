from django.shortcuts import render
from .EmailBackend import EmailBackend
from apscheduler.schedulers.background import BackgroundScheduler
from django.views.generic import ListView
from .models import File
from .forms import FileForm
from .FetchEmail import FetchEmail
import os
import imaplib
import email
from .OSguesser import DefinePath

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

@sched.scheduled_job('cron',hour="17", minute="00", second='00')
def timed_job():
    print('Downloaded attachment')
    run = EmailBackend()
    run.run_email_backend()

#sched.start()

#For testing purposes, you can mess with this code
@sched.scheduled_job('interval', seconds=5)
def timed_job():
    print('Interval')
    run = EmailBackend()
    run.run_email_backend()
sched.start()

#Views go here
def dashboard_view(request):
    return render(request, 'email_fetcher/index.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def register_view(request):
    return render(request, 'accounts/register.html')  

def mailbox_view(request):
    return render(request, 'email_fetcher/mailbox.html')

def inventory_view(request):
    return render(request, 'email_fetcher/inventory.html')

# exports a list of messages from our mailbox
def display_files_view(request):

    # fetch emails from mailbox
    user_email = 'logos.hackathon@gmail.com'
    app_password = "kyfvehptcrlpgrui"
    gmail_host = 'imap.gmail.com'
    context_object_name = 'email_messages'
    email_messages = []

    fetch_email = FetchEmail(gmail_host, user_email, app_password)
    # set connection
    mail = imaplib.IMAP4_SSL(gmail_host)
    # login
    mail.login(user_email, app_password)
    # select inbox
    mail.select("INBOX")
    # total number of mails from specific user
    email_ids = email_data[0]
    id_list = email_ids.split()
    print("Total Messages:", len(id_list))

    for num in email_data[0].split():
        _, email_data = mail.fetch(num, '(RFC822)')
        raw_email = email_data[0][1]

        # convert binary encoded 'raw_email' to UTF-8 charset
        raw_email_string = raw_email.decode('utf-8')

        # email_message is type Message => long strings of email data
        # .message_from_string helps convert it into dictionary format with required fields
        email_message = email.message_from_string(raw_email_string)

        email_messages.append(email_message)
    
    context = {
        'email_messages' : email_messages,
    }
    return render(request, 'email_fetcher/display_tmp.html', context)

# def attachments_view(request):
#     # fetch emails from mailbox
#     user_email = 'logos.hackathon@gmail.com'
#     app_password = "kyfvehptcrlpgrui"
#     gmail_host = 'imap.gmail.com'
#     context_object_name = 'email_messages'
#     email_messages = []

#     fetch_email = FetchEmail(gmail_host, user_email, app_password)
#     # set connection
#     mail = imaplib.IMAP4_SSL(gmail_host)
#     # login
#     mail.login(user_email, app_password)
#     # select inbox
#     mail.select("INBOX")

#         # select specific mails
#     # insert desired filter as parameter in .search (FROM, TO, SUBJECT...)
#     # else it'll return all emails in mailbox
#     # .search returns 2 values =>
#     # 'type' tells us whether request was 'ok' or not (set as _ to dispose afterwards)
#     # 'email_data' is id's of all the emails
#     _, email_data = mail.search(None, 'all')

#     # total number of mails from specific user
#     email_ids = email_data[0]
#     id_list = email_ids.split()
#     print("Total Messages:", len(id_list))

#     for num in email_data[0].split():
#         _, email_data = mail.fetch(num, '(RFC822)')
#         raw_email = email_data[0][1]

#         # convert binary encoded 'raw_email' to UTF-8 charset
#         raw_email_string = raw_email.decode('utf-8')

#         # email_message is type Message => long strings of email data
#         # .message_from_string helps convert it into dictionary format with required fields
#         email_message = email.message_from_string(raw_email_string)

#         email_messages.append(email_message)
    


#         #Loop through email list and 
#         # saving each attachment name into a filename list
#         filename_list = []
#         csv_format = ".csv"
#         for email_message in email_messages:
#             filename = fetch_email.getFileName(email)
#             if(filename is None):
#                 continue
#             filename_list.append(filename)


#         #Determine the path to download attachments later
#         path = DefinePath()
#         truepath = path.setPath()

#         #Set convention for file path and file name
#         for filename in filename_list:
#             #Check OS type first
#             if(path.guessWindows):
#                 #Set names for each attachment unique to OS
#                 palangWindows = "\\"
#                 xlsx_file_name = palangWindows + filename
#                 csv_file_name = palangWindows + filename + csv_format
#                 xlsx_file_path = truepath + xlsx_file_name
#                 csv_file_path = truepath + csv_file_name
#                 self.convert_xlsx_to_csv(xlsx_file_path, csv_file_path)
#             else:
#                 palangOthers = "/"
#                 xlsx_file_name = palangOthers + filename
#                 csv_file_name = palangOthers + filename + csv_format
#                 xlsx_file_path = truepath + xlsx_file_name
#                 csv_file_path = truepath + csv_file_name
#                 self.convert_xlsx_to_csv(xlsx_file_path, csv_file_path)





#     fetch_email.save_attachment(email_messages, path_to_file)

#     context = {
#         'email_messages' : email_messages,
#         'path_to_file' : path_to_file
#     }

#     return render(request, 'email_fetcher/display_tmp.html', context)
# returns all data from recent retrieved emails
