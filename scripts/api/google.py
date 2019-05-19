import os
import sys
import re

from oauth2client.client import GoogleCredentials
from google.cloud import translate

from .base import Translator


class GoogleTranslator(Translator):
    def __init__(self):
        self._client = None
        self._cred = None

        self._find_cred()
        if not self._cred:
            print('Error: credential file is not found.')
            print('put google-translate****.json into cred dir.')
            sys.exit(1)
        
        self._init_client()
        if not self._client:
            print('Error: client does not work.')
            sys.exit(1)

    def translate(self, text, source, target):
        translation = self._client.translate(text, source_language=source, target_language=target, model='nmt')
        return translation['translatedText']

    def _find_cred(self):
        cred_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'cred')
        fltr = re.compile('^google-translate([\w\-]*).json$')
        for fname in os.listdir(cred_dir):
            if fltr.search(fname):
                self._cred = os.path.join(cred_dir, fname)
                return

    def _init_client(self):
        self._client = translate.Client.from_service_account_json(self._cred)
