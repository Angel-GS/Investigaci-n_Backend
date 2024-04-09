import json
from Utilities.mailDecoder import Decoder
import Utilities.mailResponseSender as mailResponseSender 

urgentMailBox = 'raulmirandavargas82@gmail.com'
mail_Json = ' { "sender": "paratektechnologies@gmail.com", "subject": "Revisión Urgente","message": "Necesito que revisen el artículo de cambio climatico"}'

#Toma el contenido del JSON y lo pasa a un formato de correo para poder trabajarlo
mailResponse = json.loads(mail_Json, cls=Decoder)

#Dependiendo del asunto del correo, se envia una respuesta automatica
match mailResponse.subject:
    case 'Revisión Urgente':
        #Se envia un correo a la bandeja de correos urgentes
        mailResponseSender.MassiveEmailSender.send_mails(
            urgentMailBox, 
            "Correo con asunto importante",
            ("Se envió un mensaje con el asunto "+ mailResponse.subject + " , y con el contenido: \n" + mailResponse.message +" \nPara responder es al correo " + mailResponse.sender))
        #Se responde al remitente del correo
        mailResponseSender.MassiveEmailSender.send_mails(
            mailResponse.sender, 
            "Respuesta inmediata a correo urgente",
            "Su correo fue recibido y sera atendido en la mayor brevedad posible")
        print('El asunto es correcto')
    case 'Publicidad de descuentos':
        print('Recordatorio de pago')
    case 'Recordatorio de pago':
        print('Publicidad de descuentos')
    case 'Ayuda con el sistema':
         #Se envia una respuesta automatica al correo de ayuda con el sistema por si el problema es común
         mailResponseSender.MassiveEmailSender.send_mails(
            mailResponse.sender, 
            "Respuesta sobre ayuda con el sistema",
            "A continuación le brindamos una serie de opciones para solucionar su problema: \n 1. Verificar su conexión a internet \n 2. Verificar que su correo no este en la bandeja de spam \n 3. Verificar que su correo no este bloqueado por su proveedor de servicios de internet \n 4. Verificar que su correo no este bloqueado por su proveedor de servicios de correo \n Si su problema no fue resuelto contactese con nosotros y le estaremos ayudando en la brevedad posible")
