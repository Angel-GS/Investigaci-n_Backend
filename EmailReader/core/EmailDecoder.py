from email import message_from_bytes
from email.header import decode_header

class EmailDecoder:
    @staticmethod
    def decode_email(email_bytes):
        email_message = message_from_bytes(email_bytes)
        subject = decode_header(email_message["Subject"])[0][0]
        if isinstance(subject, bytes):
            subject = subject.decode('utf-8', errors='replace')

        from_address = email_message["From"]
        to_address = email_message["To"]
        body = EmailDecoder.extract_body(email_message)

        return {
            "subject": subject,
            "from_address": from_address,
            "to_address": to_address,
            "body": body
        }

    @staticmethod
    def extract_body(email_message):
        body = ""
        if email_message.is_multipart():
            for part in email_message.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                payload = part.get_payload(decode=True)
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    body += EmailDecoder.decode_payload(payload)
        else:
            content_type = email_message.get_content_type()
            payload = email_message.get_payload(decode=True)
            if content_type == "text/plain":
                body = EmailDecoder.decode_payload(payload)
        return body

    @staticmethod
    def decode_payload(payload):
        if payload:
            try:
                return payload.decode('utf-8', errors='replace')
            except UnicodeDecodeError:
                return payload.decode('ISO-8859-1', errors='replace')
        return ""
