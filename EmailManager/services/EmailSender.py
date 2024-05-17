import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.config import SMTP_CONFIG

class EmailSender: 
    @classmethod
    def send_mails(cls, receptor, subject, message):
        try:
            msg = MIMEMultipart()
            msg['From'] = SMTP_CONFIG['login_email']
            msg['To'] = receptor
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP(SMTP_CONFIG['server'], SMTP_CONFIG['port'])
            server.starttls()
            server.login(SMTP_CONFIG['login_email'], SMTP_CONFIG['login_password'])
            text = msg.as_string()
            server.sendmail(SMTP_CONFIG['login_email'], receptor, text)
            server.quit()
            print('Mail sent successfully')
        except Exception as e:
            print('Error sending mail:', e)
