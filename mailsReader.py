import imaplib
import email
from email.header import decode_header
import json
import re

class EmailReader:
    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password

    def read_emails(self):
        # Conección por medio de imap, antes usamos smtp, pero imap permite leer los adjuntos, smtp no pero la lógica es la isma
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(self.email_address, self.password)

        # aqui se agarra el inbox como bandeja de entrada que el default cuando uno entra a gmail.com
        imap.select("inbox")

        # busca todos los correos no leidos que teenga la bandeja de entrada
        _, message_numbers = imap.search(None, "UNSEEN")

        # lista para almacenar los correos que depues se pasa a json
        emails = []

        # for para recolectar todos los correos no leidos, el  _, significa que no se va a usar el primer valor que regresa el fetch, 
        # digamos la vara en el correo es asi: body: texto, entonce se salta ese texto de "body" y solo toma la info como tal del correo
        #RFC822 es un formato de correos electronicos nada más
        for num in message_numbers[0].split():
            _, message_data = imap.fetch(num, "(RFC822)")
            _, b = message_data[0]
            email_message = email.message_from_bytes(b)
            subject = decode_header(email_message["Subject"])[0][0]
            if isinstance(subject, bytes): # esto significa que si el subject es un byte, lo decodifica a utf-8, para que se vea la info en texto plano y no como bytes
                subject = subject.decode('utf-8', errors='replace')

            # agarramos solo lo que nos importa de toda la info del correo
            from_address = email_message["From"]
            to_address = email_message["To"]
            body = ""

            # y acá agarramos el cuerpo del correo, si es multipart, osea si tiene adjuntos,  se recorre cada parte del correo para recuperarlo y agregarlo
            if email_message.is_multipart():
                for part in email_message.walk(): # walk es un metodo que recorre cada parte del correo
                    content_type = part.get_content_type() # agarra el tipo de contenido del correo
                    content_disposition = str(part.get("Content-Disposition"))
                    part_body = ""
                    payload = part.get_payload(decode=True) #con este payload se agarra el contenido del correo como tal y  se decodifica
                    if payload is not None: # si el payload no es nulo, se decodifica a utf-8 de igual forma si no da error por estar vacio pero da vacio en un formato que no se entiende
                        try:
                            part_body = payload.decode('utf-8', errors='replace') # se decodifica a utf-8 todo el contenido del correo
                        except UnicodeDecodeError:
                            try:
                                part_body = payload.decode('ISO-8859-1', errors='replace') # si no se puede decodificar a utf-8, se decodifica a ISO-8859-1
                            except:
                                pass
                    if content_type == "text/plain" and "attachment" not in content_disposition: # si el contenido es texto plano y no tiene adjuntos, se agrega al cuerpo del correo
                        body += part_body
            else: # si no es multipart, osea si no tiene adjuntos, se agarra el contenido del correo como tal y se ahce lo mismo que antes
                content_type = email_message.get_content_type()
                payload = email_message.get_payload(decode=True)
                if content_type == "text/plain" and payload is not None:
                    try:
                        body = payload.decode('utf-8', errors='replace')
                    except UnicodeDecodeError:
                        try:
                            body = payload.decode('ISO-8859-1', errors='replace')
                        except:
                            pass

            
            cleaned_body = self.clean_text(body) # se limpia el cuerpo del correo para que solo quede el texto

            
            emails.append({  # se agrega el correo a la lista ya  con el formato y ordenado como queremos
                "Subject": subject,
                "From": from_address,
                "To": to_address,
                "Body": cleaned_body
            })

        # Cerrar conexión
        imap.close()
        imap.logout()

        # se pasa toda la llista a json
        emails_json = json.dumps(emails, indent=4)
        
        # Imprimir el JSON
        print(emails_json) #y se printea en la consola el json

    def clean_text(self, text): #esto es solo para limpar el texto de erroes que pueden quedar al pasar el formato de bytes a utf-8
        # Eliminar caracteres no deseados usando expresiones regulares
        cleaned_text = re.sub(r'[^\w\s]', '', text)
        return cleaned_text



email_address = "angel.leandrosg@gmail.com"  
password = "tblc xmdc kehf tkqt"

email_reader = EmailReader(email_address, password)

email_reader.read_emails()
