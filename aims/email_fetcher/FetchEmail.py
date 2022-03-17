import imaplib
import os
import email

class FetchEmail:

    connection = None
    error = None

    def __init__(self, mail_server, user_email, app_password):
        self.connection = imaplib.IMAP4_SSL(mail_server)
        self.connection.login(user_email, app_password)
        self.connection.select(readonly=False)
    
    def fetch_message(self):
        emails = []

        # change search argument based on our needs
        #unSeen - is for unread messages
        #all - is for all messages
        (result, messages) = self.connection.search(None, 'all')
        if result == "OK":
            for message in messages[0].split(b' '):
                try:
                    ret, data = self.connection.fetch(message, '(RFC822)')
                except:
                    print("No new emails to read.")
                    self.close_connection()
                    exit()

                msg = email.message_from_bytes(data[0][1])
                if isinstance(msg, str) == False:
                    emails.append(msg)
                response, data = self.connection.store(message, '+FLAGS', '\\Seen')

            return emails

        self.error = "Failed to retrieve emails."
        return emails
    
    # Given a list of messages, 
    # save all its attachments into a specified directory
    def save_attachment(self, messages_list, download_folder):
        att_path = "No attachment found."
        for part in messages_list.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            att_path = os.path.join(download_folder, filename)

            if not os.path.isfile(att_path):
                fp = open(att_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
        return att_path

    #Get just the file name
    def getFileName(filename):
        return filename
