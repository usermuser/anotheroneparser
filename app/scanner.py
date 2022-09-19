# Будет JsonFetcher и HtmlFetcher, ну и базовый класс BaseFetcher
# В зависимости от типа, будет использоваться тот или иной Fetcher.
# У всех стратегий будет метод Fetch

from bs4 import BeautifulSoup, Tag


class DataType:
    pass


class BaseFetcher:
    """todo docstring missing"""
    def __init__(self, type: DataType):  # todo use strategy pattern here.
        self.type = type

    def fetch(self):
        raise NotImplemented


class JsonFetcher:
    pass


class XmlFetcher:
    pass


class HtmlFetcher:
    """todo docstring missing

    type = DataType.get_type()                          # sync
    new_urls = UrlsGetter.get_url(page, content_type)   # sync
    urls_saver = RedisSaver().save(new_urls)            # can be CsvSaver().save()   # async
    dq = SimpleDequeue().add(urls)                      # can be both
    """

    def fetch(self):
        pass
