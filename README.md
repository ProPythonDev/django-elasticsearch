Search app for oscar using elasticsearch
========================================

Setup
-----

The following apps need to be added to ``INSTALLED_APPS``

```
"oscar_elasticsearch.search", # replace standard oscar app
"wagtail.contrib.search_promotions", # allow search result display and such
"wagtail.search", # maybe you need this I'm not sure, maybe more is needed

```

Settings required to replace the search app

```
OSCAR_ELASTICSEARCH_QUERY_PAGE_SIZE = 20
OSCAR_PRODUCT_SEARCH_HANDLER = "oscar_elasticsearch.search.search_handlers.ProductSearchHandler",
OSCAR_SEARCH = {
    "DEFAULT_ITEMS_PER_PAGE": 20,
    "MONTHS_TO_RUN_ANALYTICS": 3,
    "FACETS": [
        {
            "name": "price",
            "label": "Price",
            "type": "range",
            "formatter": "oscar_elasticsearch.search.format.currency",
            "ranges": [
                25,
                100,
                500,
                1000
            ]
        },
        {
            "name": "attrs.gewicht",
            "label": "Gewicht",
            "type": "term",
            "ranges": []
        },
        {
            "name": "attrs.googleshopping",
            "label": "Google product",
            "type": "term",
            "ranges": []
        },
        {
            "name": "attrs.size",
            "label": "Maat",
            "type": "term",
            "ranges": []
        },
        {
            "name": "attrs.height",
            "label": "Hoogte",
            "type": "term",
            "ranges": []
        },
        {
            "name": "attrs.zult",
            "label": "Datum",
            "type": "term",
            "ranges": []
        },
        {
            "name": "attrs.stroomverbruik",
            "label": "Stroomverbruik",
            "type": "term",
            "ranges": []
        },
        {
            "name": "attrs.bijzonderheden",
            "label": "Bijzonderheden",
            "type": "term",
            "ranges": []
        }
    ]
}
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "oscar_elasticsearch.search.search",
        "URLS": ["http://127.0.0.1:9200"],
        "INDEX": "my-index-name",
        "TIMEOUT": 120,
        "OPTIONS": {},
        "INDEX_SETTINGS": {},
        "ATOMIC_REBUILD": True,
        "AUTO_UPDATE": True,
    }
}
```