from services.EmailReader import EmailReader
from core.EmailProcessor import EmailProcessor
from config.config import SMTP_CONFIG

if __name__ == '__main__':
    email_reader = EmailReader(SMTP_CONFIG['email_address'], SMTP_CONFIG['password'])
    email_processor = EmailProcessor()

    email_reader.connect()
    message_numbers = email_reader.fetch_unseen_emails()

    for num in message_numbers:
        email_bytes = email_reader.fetch_email(num)
        email_processor.process_email(email_bytes)

    email_reader.close_connection()
