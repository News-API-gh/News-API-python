import requests

from api.exceptions import UnauthorizedException
from api.article import Article
from api.source import Source
from api.response import Response

base_url = "https://newsapi.org/v2/"

class News(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def list_sources(self, **kwargs):
        estring = "sources"
        r = self._news_request(estring=estring, **kwargs)
        status = r.get("status", None)
        total_results = r.get("totalResults", 0)
        sources = r.get("sources", [])
        sources_objs = [self._populate_attributes(Source(), d) for d in sources]
        return self._populate_attributes(Response(), {"total_results": totalResults, "status": status, "sources": sources_objs})
    
    def get_everything(self, **kwargs):
        estring = "everything"
        r = self._news_request(estring=estring, **kwargs)
        status = r.get("status")
        total_results = r.get("totalResults")
        articles = r.get('articles')
        article_objs = [self._populate_attributes(Article(), d) for d in articles]
        return self._populate_attributes(Response(), {"total_results": total_results, "status": status, "articles": article_objs})
        
    def get_top_headlines(self, **kwargs):
        estring = "top-headlines"
        response = self._news_request(estring=estring, **kwargs)
        r = self._news_request(estring=estring, **kwargs)
        status = r.get("status")
        total_results = r.get("totalResults")
        articles = r.get('articles')
        article_objs = [self._populate_attributes(Article(), d) for d in articles]
        return self._populate_attributes(Response(), {"total_results": total_results, "status": status, "articles": article_objs})

    def _news_request(self, estring, **kwargs):
        return self._make_request(end_point=estring, queries=kwargs)

    def _make_request(self, end_point, queries=None):
        url = base_url+end_point        
        headers = {'X-Api-Key': self.api_key}
        r = requests.get(url, headers=headers, params=queries)
        if r.status_code == 200:
            return r.json()
        elif r.status_code == 401:
            raise UnauthorizedException(r.json())
        
    def _populate_attributes(self, obj, attr_dict):
        for key, value in attr_dict.iteritems():
            setattr(obj, key, value)
        return obj
