class NewsAPIError(Exception):

    def __init__(self,  response_json, *args, **kwargs):
        message = '{code} : {message}'.format(**response_json)
        super().__init__(message, *args, **kwargs)