from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.desumoin

def list_authors():
    """List the people we have quotations for.
    """
    return sorted(db.quotes.distinct('authors'))

def add_quote(authors, text, context, tags, featuring):
    """Add a quote to the database.

    Parameters
    ==========
    authors : list of Author
    text : str
    context : str
    tags : list of str
    featuring : list of Author
    """

    return db.quotes.insert_one({
        'authors': [a.name for a in authors],
        'text': text,
        'context': context,
        'tags': tags,
        'featuring': [f.name for f in featuring]
    })