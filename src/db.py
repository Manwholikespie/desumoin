from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.desumoin


def list_authors():
    """List the people we have quotations for.
    """
    return sorted(db.quotes.distinct('authors'))


def list_all_quotes():
    """List all the quotes we have.
    """
    return reversed([*db.quotes.find({})])


def find_quotes_by_author(authorName):
    """Finds all quotes by an author.
    """
    return reversed([*db.quotes.find({
        'authors': authorName
    })])


def add_quote(authors, text, context):
    """Add a quote to the database.

    Parameters
    ==========
    authors : list of Author
    text : str
    context : str
    """
    # TODO: Re-implement tags when we're ready.
    return db.quotes.insert_one({
        'authors': authors,
        'text': text,
        'context': context
    })
