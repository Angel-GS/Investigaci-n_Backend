import re

class TextCleaner:
    def clean_text(self, text):
        return re.sub(r'[^\w\s]', '', text)
