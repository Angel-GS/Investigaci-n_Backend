import smtplib  #protocolo de comunicacion para enviar y recibir correos electronicos
from email.mime.text import MIMEText            #forman el cuerpo del mensaje
from email.mime.multipart import MIMEMultipart  
import random 
import time
class MassiveEmailSender: 
    
    def __init__(self, sender_mail, password): #constructor
        self.sender_mail = sender_mail
        self.password = password

    def send_mails(self, receptor, subject, message):
        try: 
            msg = MIMEMultipart()
            msg['From'] = self.sender_mail
            msg['To'] = receptor
            msg['Subject'] = subject
            
            msg.attach(MIMEText(message, 'plain'))#adjuntar el mensaje al cuerpo del correo
            
            #conección con el servidor de correo
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.sender_mail, self.password)
            text = msg.as_string()
            server.sendmail(self.sender_mail, receptor, text)
            server.quit()
            print('Mail send successfully')
        except Exception as e:
            print('Error sending mail: ', e)

#Datos para el envio de correos
sender_mail = 'paratektechnologies@gmail.com'
password = 'syou jgln cixq qfbg'

#instancia de la clase
massiveEmailSender = MassiveEmailSender(sender_mail, password)
#receptor del correo
receptor = 'raulmirandavargas82@gmail.com'

#cuerpo del correo 
subjects = ['Publicidad de descuentos', 'Revición Urgente', 'Recordatorio de pago ', 'Ayuda con el sistema'] #lista de asuntos

message = 'Hola, este es un mensaje de prueba'

#envio de 30 por minuto, durante 10 minutos, 300 correos  
for i in range(300): 
    subject = random.choice(subjects)
    #un case que verifique el asunto, y personalice el mensaje (Raux)(diccionario)
    
    massiveEmailSender.send_mails(receptor, subject, message)
    time.sleep(6)







            
            
            
            
            
            