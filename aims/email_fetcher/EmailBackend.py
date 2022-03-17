import FetchEmail

class EmailBackend:

    #Method to access email, fetch messages and save attachment
    def run_backend(self):

        #Access Details
        user_email = 'logos.hackathon@gmail.com'
        app_password = "kyfvehptcrlpgrui"
        gmail_host = 'imap.gmail.com'

        #initialize connection
        get_email = FetchEmail(gmail_host, user_email, app_password)

        #Get the list of email
        email_list = get_email.fetch_message()

        #Loop through list and saving every attachment of the email into local directory
        for email in email_list:
            get_email.save_attachment(email,'C:\\Users\\User\\Documents\\Attachment')

