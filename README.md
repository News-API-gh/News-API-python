# News API SDK for Python
Coming soon... this is where our officially supported SDK for Python is going to live.

***

## Developers... we need you!
We need some help fleshing out this repo. If you're a Python dev with experience building PyPI-compatible libraries and web API wrappers, we're offering a reward of $250 to help us get started. For more info please email support@newsapi.org, or dive right in and send us a pull request.


# Usage
```
import newsapi
newsapi.API_KEY = '<API Key>'

# list of all sources
newsapi.Sources().list()

# list of American sources
newsapi.Sources().list(country='us')

# list of American Gaming sources
newsapi.Sources().list(**{'country': 'us', 'category': 'gaming'})

# Same pattern for TopHeadlines and Everything

newsapi.TopHeadlines().list()
newsapi.TopHeadlines().list(arg1=..., arg2=...)
newsapi.TopHeadlines().list(**{'arg1':..., 'arg2':...})

newsapi.Everything().list()
newsapi.Everything().list(arg1=..., arg2=...)
newsapi.Everything().list(**{'arg1':..., 'arg2':...})
```
