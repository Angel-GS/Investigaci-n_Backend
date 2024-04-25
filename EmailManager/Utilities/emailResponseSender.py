import smtplib  #protocolo de comunicacion para enviar y recibir correos electronicos
from email.mime.text import MIMEText            #forman el cuerpo del mensaje
from email.mime.multipart import MIMEMultipart  

class MassiveEmailSender: 
    @classmethod
    def send_mails(self, receptor, subject, message):
        try: 
            msg = MIMEMultipart()
            msg['From'] = 'paratektechnologies@gmail.com'
            msg['To'] = receptor
            msg['Subject'] = subject
            
            msg.attach(MIMEText(message, 'plain'))#adjuntar el mensaje al cuerpo del correo
            
            #conexión con el servidor de correo
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('paratektechnologies@gmail.com', 'syou jgln cixq qfbg')
            text = msg.as_string()
            server.sendmail('paratektechnologies@gmail.com', receptor, text)
            server.quit()
            print('Mail send successfully')
        except Exception as e:
            print('Error sending mail: ', e)
