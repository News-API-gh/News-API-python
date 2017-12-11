# News API SDK for Python

## Installation
Download this repository on your machine, then open a terminal in the folder. To install type:
```bash
python setup.py install
```
(please note that sudo may be required)
To check the installation, open a terminal and type:
```bash
python
```
then, try to import the package:
```python3
 from newsapi import newsapi
```
If no error appears, the package have been succesfully installed.

##Example
```python3
from newsapi import newsapi

apiKey = "2809dbe4cfe044708cacd93879af483e"

#Get the list of sources
newsapi.getSources(apiKey = apiKey)
#get the list of sources in italian
newsapi.getSources(apiKey = apiKey, language="it")
#get the list of sources from germany
newsapi.getSources(apiKey = apiKey,country="de")


#Get all articles about Bitcoin
newsapi.getEverything(apiKey = apiKey,q="Bitcoin")
#All articles mentioning Apple from yesterday, sorted by popular publishers first
newsapi.getEverything(apiKey = apiKey,q="Apple",dateFrom="2017-12-10",sortBy="popularity")
#All articles published by the WSJ and NY Times
newsapi.getEverything(apiKey,source="the-wall-street-journal,the-new-york-times")

#Top headlines from BBC News
newsapi.getTopHeadlines(apiKey=apiKey,source="bbc-news")
#Top headlines from The Next Web and The Verge
newsapi.getTopHeadlines(apiKey=apiKey,source="the-next-web,the-verge")
#Top headlines about Trump
newsapi.getTopHeadlines(apiKey=apiKey,q="Trump")
#Top headlines from business sources in English
newsapi.getTopHeadlines(apiKey=apiKey,category="business",language="en")
```
