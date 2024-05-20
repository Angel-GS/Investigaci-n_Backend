from services.KafkaProducer import EmailProducer
from utilities.TextCleaner import TextCleaner
from core.EmailDecoder import EmailDecoder

class EmailProcessor:
    def __init__(self):
        self.email_producer = EmailProducer()
        self.text_cleaner = TextCleaner()

    def process_email(self, email_bytes):
        email_message = EmailDecoder.decode_email(email_bytes)
        cleaned_body = self.text_cleaner.clean_text(email_message['body'])

        self.email_producer.produce_email("emails", {
            "subject": email_message['subject'],
            "sender": email_message['from_address'],
            "to": email_message['to_address'],
            "message": cleaned_body
        })
