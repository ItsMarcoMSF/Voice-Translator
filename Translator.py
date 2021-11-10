from googletrans import Translator


class Trans:
    def __init__(self):
        self.p = Translator()

    def trans(self, phrase):
        k = self.p.translate(phrase, dest='french', src='en')
        translated = str(k.text)
        return translated
