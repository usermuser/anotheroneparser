# Here we will implement strategy pattern
# to be able to change parsing strategy on the fly
# but first we have to check what kind of response we got
# for example if we received xml -> use XmlParser
# for json -> JsonParser, and so on.
from enum import Enum

from bs4 import BeautifulSoup

from app.exceptions import UnknownTypeError, FileFetcherNotFound
from app.scanner import HtmlParser, JsonParser

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


class FileType(Enum):
    HTML = 'html'
    JSON = 'json'
    CSV = 'csv'
    XML = 'xml'


class TypeGetter:

    @staticmethod
    def get_type(page):
        if page.startswith('<html>'):
            return 'html'
        if page.startswith('{"a":1,"b":2}'):
            return 'json'
        raise UnknownTypeError


class UrlsParser:
    """todo docstring missing"""

    _FILE_TYPE_GETTER = TypeGetter()

    def _get_strategy(self, file_type):
        if file_type == FileType.HTML:
            return HtmlParser()
        if file_type == FileType.JSON:
            return JsonParser()
        raise FileFetcherNotFound

    def get_urls(self, page):
        file_type = self._FILE_TYPE_GETTER.get_type(page)
        parser = self._get_strategy(file_type)
        return parser.parse()


urls = UrlsParser().get_urls(html_doc)
