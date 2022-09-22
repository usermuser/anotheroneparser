# Будет JsonFetcher и HtmlFetcher, ну и базовый класс BaseFetcher
# В зависимости от типа, будет использоваться тот или иной Fetcher.
# У всех стратегий будет метод Fetch

from bs4 import BeautifulSoup, Tag
from abc import ABC, abstractmethod

from app.data_types import DataType


class BaseParser(ABC):
    """todo docstring missing"""

    @abstractmethod
    def parse(self):
        raise NotImplemented


class JsonParser(BaseParser):
    """todo docstring missing"""

    def parse(self):
        pass


class XmlParser(BaseParser):
    """todo docstring missing"""

    def parse(self):
        pass


class HtmlParser(BaseParser):
    """todo docstring missing"""

    def parse(self):
        pass


# if __name__ == '__main__':
    # type = DataType.get_type()                          # sync
    # new_urls = UrlGetter.get_url(page, type)            # sync
    # urls_saver = RedisSaver().save(new_urls)            # can be CsvSaver().save()   # async
    # dq = SimpleDequeue().add(urls)                      # can be both

