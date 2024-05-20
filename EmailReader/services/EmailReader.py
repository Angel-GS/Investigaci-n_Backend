import imaplib

class EmailReader:
    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password

    def connect(self):
        self.imap = imaplib.IMAP4_SSL("imap.gmail.com")
        self.imap.login(self.email_address, self.password)
        self.imap.select("inbox")

    def fetch_unseen_emails(self):
        _, message_numbers = self.imap.search(None, "UNSEEN")
        return message_numbers[0].split()

    def fetch_email(self, num):
        _, message_data = self.imap.fetch(num, "(RFC822)")
        return message_data[0][1]

    def close_connection(self):
        self.imap.close()
        self.imap.logout()
