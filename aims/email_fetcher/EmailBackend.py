from .FetchEmail import FetchEmail
import pandas as pd
import os
from .OSguesser import DefinePath
import platform
class EmailBackend:

    #Method to access email, fetch messages and save attachment
    def run_email_backend(self):

        #Access Details
        user_email = 'logos.hackathon@gmail.com'
        app_password = "kyfvehptcrlpgrui"
        gmail_host = 'imap.gmail.com'

        #Determine the path to download attachments later
        path = DefinePath()
        truepath = path.setPath()

        #initialize connection
        get_email = FetchEmail(gmail_host, user_email, app_password)

        #Get the list of email
        email_list = get_email.fetch_message()

        #Loop through list and saving every attachment of the email into local directory
        for email in email_list:
            get_email.save_attachment(email,truepath)

        #Loop through email list and saving each attachment name into a filename list
        filename_list = []
        csv_format = ".csv"
        for email in email_list:
            filename = get_email.getFileName(email)
            if(filename is None):
                continue
            filename_list.append(filename)

        #Set convention for file path and file name
        for filename in filename_list:
            #Check OS type first
            if(path.guessWindows):
                #Set names for each attachment unique to OS
                palangWindows = "\\"
                xlsx_file_name = palangWindows + filename
                csv_file_name = palangWindows + filename + csv_format
                xlsx_file_path = truepath + xlsx_file_name
                csv_file_path = truepath + csv_file_name
                self.convert_xlsx_to_csv(xlsx_file_path, csv_file_path)
            else:
                palangOthers = "/"
                xlsx_file_name = palangOthers + filename
                csv_file_name = palangOthers + filename + csv_format
                xlsx_file_path = truepath + xlsx_file_name
                csv_file_path = truepath + csv_file_name
                self.convert_xlsx_to_csv(xlsx_file_path, csv_file_path)

    # Method to convern .xlsx filetype to .csv filetype
    def convert_xlsx_to_csv(self, xlsx_file_path, converted_csv_file_path):
        read_file = pd.read_excel(xlsx_file_path)
        read_file.to_csv(converted_csv_file_path, index = None, header=True)