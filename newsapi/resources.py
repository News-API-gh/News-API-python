from .client import Client


class BaseResource:

    endpoint = None
    item = None

    def __init__(self):
        self.client = Client()

    def list(self, **params):
        return self.client.get(self.endpoint, params)[self.item]


class TopHeadlines(BaseResource):

    endpoint = 'top-headlines'
    item = 'articles'


class Everything(BaseResource):

    endpoint = 'everything'
    item = 'articles'


class Sources(BaseResource):

    endpoint = 'sources'
    item = 'sources'
