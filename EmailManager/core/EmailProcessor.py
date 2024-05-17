import json
from utilities.EmailDecoder import EmailDecoder
from services.EmailSender import EmailSender
from config.config import URGENT_MAILBOX

def process_email(email_json):
    mail_response = json.loads(email_json, cls=EmailDecoder)

    sender = mail_response.sender
    subject = mail_response.subject
    message = mail_response.message

    if subject == 'Revisión Urgente':
        EmailSender.send_mails(
            URGENT_MAILBOX, 
            "Correo con asunto importante",
            f"Se envió un mensaje con el asunto {subject}, y con el contenido:\n{message}\nPara responder es al correo {sender}"
        )
        EmailSender.send_mails(
            sender, 
            "Respuesta inmediata a correo urgente",
            "Su correo fue recibido y será atendido en la mayor brevedad posible"
        )
        print('El asunto es correcto')
    elif subject == 'Publicidad de descuentos':
        print('Publicidad de descuentos')
    elif subject == 'Recordatorio de pago':
        print('Recordatorio de pago')
    elif subject == 'Ayuda con el sistema':
        EmailSender.send_mails(
            sender, 
            "Respuesta sobre ayuda con el sistema",
            "A continuación le brindamos una serie de opciones para solucionar su problema:\n1. Verificar su conexión a internet\n2. Verificar que su correo no esté en la bandeja de spam\n3. Verificar que su correo no esté bloqueado por su proveedor de servicios de internet\n4. Verificar que su correo no esté bloqueado por su proveedor de servicios de correo\nSi su problema no fue resuelto, contáctese con nosotros y le estaremos ayudando en la brevedad posible"
        )