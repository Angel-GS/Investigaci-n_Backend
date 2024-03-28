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
subjects = ['Publicidad de descuentos', 'Revisión Urgente', 'Recordatorio de pago ', 'Ayuda con el sistema'] #lista de asuntos


publicityMessages = ['Buenos días, quería por favor, cancelar mi suscripción a su publicidad',
                     'Buenos días, me gustaría saber si tienen algún descuento en sus productos', 
                     'Buenos días, quiero suscribirme a su diario']

urgentMessages = ['Buenos días, necesito que se revise urgentemente el articulo sobre la vacuna contra el covid-19',
                  'Buenos días, necesito hacer una queja sobre el contenido de su diario',
                  'Buenos días, necesito que se revise urgentemente el articulo sobre el cambio climático']

paymentMessages = ['Buenos días, quería recordarles que ya cancelé la suscripción de este mes',
                   'Buenos días, necesito que me envíen mi factura a mi correo',
                   'Buenos días, quisiera que me enviaran un desglose de mi factura']

systemMessages = ['Buenos días, necesito ayuda con el sistema de su diario, no puedo encontrar mis métodos de pago',
                  'Buenos días, necesito ayuda con la suscripción de su diario, no puedo acceder a mi cuenta',
                  'Buenos días, necesito ayuda con la aplicación de su diario, no puedo encontrar los artículos que me interesan']


#envio de 30 por minuto, durante 10 minutos, 300 correos  
for i in range(5): 
    subject = random.choice(subjects)
    #un case que verifique el asunto, y personalice el mensaje (Raux)(diccionario)
    message = ''

    case = subject
    if case == 'Publicidad de descuentos':
        message = random.choice(publicityMessages)
    elif case == 'Revisión Urgente':
        message = random.choice(urgentMessages)
    elif case == 'Recordatorio de pago':
        message = random.choice(paymentMessages)
    elif case == 'Ayuda con el sistema':
        message = random.choice(systemMessages)
    else:
        message = 'Buenos días, quería recordarles que ya cancelé la suscripción de este mes'
    massiveEmailSender.send_mails(receptor, subject, message)
    time.sleep(6)







            
            
            
            
            
            