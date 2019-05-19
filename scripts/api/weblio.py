import sys
from urllib import parse
import requests

from bs4 import BeautifulSoup

from .base import Translator


class WeblioTranslator(Translator):
    def translate(self, text, source, target):
        html = self._get_html(text, source, target)
        return self._parse(text, html)
    
    def _get_html(self, text, source, target):
        word = parse.quote_plus(text)
        url = 'http://ejje.weblio.jp/content/'
        res = requests.get(url + word)
        return res.content
    
    def _parse(self, source_text, html):
        soup = BeautifulSoup(html, 'html.parser')
        translation = soup.find('meta', attrs={'name':'twitter:description'})
        if not translation:
            print('Error: Not supported page.')
            sys.exit(1)
        result = translation['content']
        splitter = ','
        if splitter not in result and ';' in result:
            splitter = '; '
        return result.replace(source_text + ': ', '').replace(splitter, '\n')
