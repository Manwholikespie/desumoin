from bson.objectid import ObjectId

from elasticsearch import Elasticsearch

es = Elasticsearch()


def list_authors():
    """List the people we have quotations for.
    """
    query = {
        "size": 0,
        "aggs": {
            "uniq_authors": {
                "terms": {
                    "field": "authors.keyword",
                    "size": 10000
                }
            }
        }
    }
    hits = es.search(index="desumoin", body=query, size=10000)
    return sorted([
        hit.get('key')
        for hit in
        hits.get('aggregations', {}).get('uniq_authors', {}).get('buckets', [])
    ])


def list_all_quotes():
    """List all the quotes we have.
    """
    query = {
        "query": {
            "match_all": {}
        }
    }
    hits = es.search(index="desumoin", body=query, size=10000)
    return [
        hit.get('_source')
        for hit in
        sorted(hits.get('hits', {}).get('hits', []),
               key=lambda x: x['_id'], reverse=True)
    ]


def find_quotes_by_author(authorName):
    """Finds all quotes by an author, returning them sorted by newest first.
    """
    query = {
        "query": {
            "match": {
                "authors": authorName
            }
        }
    }
    hits = es.search(index="desumoin", body=query, size=10000)
    return [
        hit.get('_source')
        for hit in
        sorted(hits.get('hits', {}).get('hits', []),
               key=lambda x: x['_id'], reverse=True)
    ]


def add_quote(authors, text, context):
    """Add a quote to the database.

    Parameters
    ==========
    authors : list of Author
    text : str
    context : str
    """
    # TODO: Re-implement tags when we're ready.
    doc = {
        'authors': authors,
        'text': text,
        'context': context
    }
    response = es.index(index='desumoin',
                        doc_type='quote',
                        id=ObjectId(),
                        body=doc)
    return response.get('result')
