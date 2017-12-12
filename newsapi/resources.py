from .client import Client


class BaseResource:

    endpoint = None

    def list(self, **params):
        client = Client()
        return client.get(self.endpoint, params)


class TopHeadlines(BaseResource):

    endpoint = 'top-headlines'

    def list(self, **params):
        return super().list(**params)['articles']


class Everything(BaseResource):

    endpoint = 'everything'

    def list(self, **params):
        return super().list(**params)['articles']


class Sources(BaseResource):

    endpoint = 'sources'

    def list(self, **params):
        return super().list(**params)['sources']
