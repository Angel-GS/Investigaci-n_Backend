import json
from mailFormat import mailFormat
# Clase que recibe los correos de formato JSON
class Decoder(json.JSONDecoder):
    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)
    #Toma el objeto JSON y lo convierte en un objeto de la clase mail
    def object_hook(self, json_dict):
        new_mail = mailFormat(
            json_dict.get('sender'), 
            json_dict.get('subject'), 
            json_dict.get('message')
            )
        
        return new_mail


    