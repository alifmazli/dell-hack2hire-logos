from .FetchEmail import FetchEmail
import pandas as pd

class EmailBackend:
        
    #Method to access email, fetch messages and save attachment
    def run_email_backend(self):

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
            #Alep: To revise this method
            get_email.save_attachment(email,'C:\\Users\\User\\Documents\\Attachment')

        #Only works on your machine if you specify the directory correctly
        #Only works on WANJO's ACER NITRO 5 GTX1650
        xlsx_file_path = "C:\\Users\\User\\Documents\\Attachment\\Marks Table.xlsx"
        csv_file_path = "C:\\Users\\User\\Documents\\Attachment\\Marks Table.csv"

        self.convert_xlsx_to_csv(xlsx_file_path, csv_file_path)

    # Method to convern .xlsx filetype to .csv filetype
    # xlsx_file_path must be in this form => "path\\to\\xlsx\\file\\sample.xlsx"
    # csv_file_path must be in this form => "path\\to\\csv\\file\\sample.csv" <== attach your desired csv file name
    def convert_xlsx_to_csv(self, xlsx_file_path, converted_csv_file_path):
        read_file = pd.read_excel(xlsx_file_path)
        read_file.to_csv(converted_csv_file_path, index = None, header=True)