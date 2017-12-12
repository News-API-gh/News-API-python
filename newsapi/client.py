import requests
from . errors import NewsAPIError


class Client:

    def __init__(self, api_url_base, timeout=80):
        self._timeout = timeout
        self._session = requests.Session()

        from newsapi import API_KEY
        self._api_key = API_KEY
        self._session.headers.update({'Authorization': self._api_key})

        self._api_url_base = api_url_base

    def get(self, endpoint, params):
        resp = self._session.get(self._api_url_base + endpoint, params=params)
        try:
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.HTTPError:
            raise NewsAPIError(resp.json())