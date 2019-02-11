# 2 configurable views
# one with all info and one just to get the overview,
# perhaps it could be reduced even more
# i am able to reduce the amount of data transfered by this


def to_list_view(article):
    return {
        'metadata': {
            'newid': article['metadata']['newid'],
            'oldid': article['metadata']['oldid'],
            'cgisplit': article['metadata']['cgisplit'],
            'lewissplit': article['metadata']['lewissplit'],
            'topics': article['metadata']['topics']
        },
        'fulltext': {
            'title': article['fulltext']['title'],
            'dateline': article['fulltext']['dateline'],
        },
        'topics': article['topics'],
        'places': article['places'],
        'people': article['people'],
        'orgs': article['orgs'],
        'companies': article['companies'],
        'topics': article['topics'],
        'date': article['date']
    }


def to_detail_view(article):
    return {
        'metadata': {
            'newid': article['metadata']['newid'],
            'oldid': article['metadata']['oldid'],
            'cgisplit': article['metadata']['cgisplit'],
            'lewissplit': article['metadata']['lewissplit'],
            'topics': article['metadata']['topics']
        },
        'fulltext': {
            'title': article['fulltext']['title'],
            'dateline': article['fulltext']['dateline'],
            'body': article['fulltext']['body'],
        },
        'topics': article['topics'],
        'places': article['places'],
        'people': article['people'],
        'orgs': article['orgs'],
        'companies': article['companies'],
        'topics': article['topics'],
        'date': article['date']
    }
