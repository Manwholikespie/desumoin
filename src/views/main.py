from pprint import pprint
from functools import reduce

import flask

import src.db as db

app = flask.current_app
bp = flask.Blueprint('main', __name__)


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


@bp.route('/author/<authorName>')
def author(authorName):
    quotes = []
    for q in db.find_quotes_by_author(authorName):
        citation = '~ ' + ', '.join([name.title() for name in q['authors']])
        if q['context']:
            citation += ', ' + q['context']
        
        quotes.append({
            'text': q['text'],
            'citation': citation
        })
    
    return flask.render_template('author.html', quotes=quotes)