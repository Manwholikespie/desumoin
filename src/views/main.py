from pprint import pprint
from functools import reduce

import flask

import src.db as db

app = flask.current_app
bp = flask.Blueprint('main', __name__)


def quote_to_dict(quote):
    """Transform the quote document from the way it is stored in our db to a
    form whose parts can be easily rendered.
    """
    citation = '~ ' + ', '.join([name.title() for name in quote['authors']])
    if quote['context']:
        citation += ', ' + quote['context']

    return {
        'text': quote['text'],
        'citation': citation
    }


@bp.route('/')
def index():
    """Return a page displaying a list of our authors.
    """
    authors = db.list_authors()
    return flask.render_template('index.html', authors=authors)


@bp.route('/submit', methods=['GET', 'POST'])
def submit():
    if flask.request.method == 'POST':
        db.add_quote(
            flask.request.form.getlist('authors[]'),
            flask.request.form['text'],
            flask.request.form['context']
        )
        return 'success'

    return flask.render_template('submit.html')


@bp.route('/all')
def all():
    """Show all the quotes we have in our database.
    """
    quotes = [quote_to_dict(q) for q in db.list_all_quotes()]
    return flask.render_template('author.html', quotes=quotes)


@bp.route('/author/<authorName>')
def author(authorName):
    quotes = [quote_to_dict(q) for q in db.find_quotes_by_author(authorName)]
    return flask.render_template('author.html', quotes=quotes)


@bp.route('/admin', methods=['GET', 'POST'])
def admin():
    """Admin dashboard for editing authors and quotes.
    """
    # TODO: Finish the implementation of this.
    # TODO: Authentication?
    data = {
        'quotes': db.list_all_quotes(),
        'authors': db.list_authors()
    }
    return flask.render_template('admin.html', data=data)