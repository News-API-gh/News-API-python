# News API SDK for Python

## Installation

```shell
pip install news-api
```

## Usage

### Initilisation

```python
from api.news import News

n = News(api_key=<api_key>)
```

### Sources

```python
n.list_sources()
```

### Everything

```python
n.get_everything(q="bitcoin")
```

### Top Headlines

```python
n.get_top_headlines(q="bitcoin")
```