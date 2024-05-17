import json
from utilities.EmailFormat import EmailFormat # type: ignore

class EmailDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, json_dict):
        return EmailFormat(
            json_dict.get('sender'), 
            json_dict.get('subject'), 
            json_dict.get('message')
        )




    
