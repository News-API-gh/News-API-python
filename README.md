# News API SDK for Python
Coming soon... this is where our officially supported SDK for Python is going to live.

***

## Developers... we need you!
We need some help fleshing out this repo. If you're a Python dev with experience building PyPI-compatible libraries and web API wrappers, we're offering a reward of $250 to help us get started. For more info please email support@newsapi.org, or dive right in and send us a pull request.

## Usage

```
from news_api import Client

news_api_client = Client('<api_key>')

top_headlines = news_api_client.top_headlines(q='bitcoin')

trump_news = news_api_client.everything(q='trump', language='en', sort_by='popularity')

sources = news_api_client.sources()
```
