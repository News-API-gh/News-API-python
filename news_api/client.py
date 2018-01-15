import requests

from news_api import const


class NewsAPIException(Exception):
    def __init__(self, response_body):
        msg = '{}: {}'.format(response_body['code'], response_body['message'])
        super(NewsAPIException, self).__init__(msg)


class Client(object):

    def __init__(self, api_key):
        self.API_KEY = api_key

    def __get(self, url, params):
        params['apiKey'] = self.API_KEY

        r = requests.get(url, params=params)

        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())

        return r.json()

    def top_headlines(self, sources=None, q=None, category=None, language=None,
                      country=None):
        params = {}

        if sources is not None:
            params['sources'] = ','.join(sources)

        if q is not None:
            params['q'] = q

        if category is not None:
            if category not in const.CATEGORIES:
                raise ValueError('Invalid category')

            params['category'] = category

        if language is not None:
            if language not in const.LANGUAGES:
                raise ValueError('Invalid language')

            params['language'] = language

        if country is not None:
            if country not in const.COUNTRIES:
                raise ValueError('Invalid country')

            params['country'] = country

        response_body = self.__get(const.TOP_HEADLINES_URL, params)

        return response_body['articles']

    def everything(self, q=None, sources=None, domains=None, oldest=None,
                   newest=None, language=None, sort_by=None, page_size=None,
                   page=None):
        params = {}

        if q is not None:
            params['q'] = q

        if sources is not None:
            params['sources'] = ','.join(sources)

        if domains is not None:
            params['domains'] = ','.join(domains)

        if oldest is not None:
            params['from'] = oldest

        if newest is not None:
            params['to'] = newest

        if language is not None:
            if language not in const.LANGUAGES:
                raise ValueError('Invalid language')

            params['language'] = language

        if sort_by is not None:
            if sort_by not in const.SORT_BY:
                raise ValueError('Invalid sort_by')

            params['sortBy'] = sort_by

        if page_size is not None:
            params['pageSize'] = page_size

        if page is not None:
            params['page'] = page

        response_body = self.__get(const.EVERYTHING_URL, params)

        return response_body['articles']

    def sources(self, category=None, language=None, country=None):
        params = {}

        if category is not None:
            if category not in const.CATEGORIES:
                raise ValueError('Invalid category')

            params['category'] = category

        if language is not None:
            if language not in const.LANGUAGES:
                raise ValueError('Invalid language')

            params['language'] = language

        if country is not None:
            if country not in const.COUNTRIES:
                raise ValueError('Invalid country')

            params['country'] = country

        response_body = self.__get(const.SOURES_URL, params)

        return response_body['sources']
