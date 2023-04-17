import json

from calibre_plugins.ebook_translator.engines.base import Base
from calibre_plugins.ebook_translator.utils import _z


load_translations()


class GoogleTranslate(Base):
    name = 'Google'
    support_lang = 'google.json'
    endpoint = 'https://translate.googleapis.com/translate_a/single'
    need_api_key = False

    def translate(self, text):
        sl = self._get_source_code()
        tl = self._get_target_code()

        return self.get_result(self.endpoint, {
            'client': 'gtx',
            'sl': sl,
            'tl': tl,
            'dt': 't',
            'q': text,
        })

    def parse(self, data):
        return ''.join(i[0] for i in json.loads(data)[0])
