from pprint import pprint
from functools import reduce

import flask

import src.auth as auth
import src.db as db
from src.models import User

import flask_login

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
    if not flask_login.current_user.is_authenticated:
        return flask.render_template('gate.html')
    authors = db.list_authors()
    return flask.render_template('index.html', authors=authors)


@bp.route('/gate', methods=['POST'])
def gate():
    credentials = flask.request.form['passphrase']

    u = User()
    u.verify_credentials(credentials, app.config['SECRET_PASSPHRASE'])
    if u.is_authenticated():
        auth.add_user(u.id)
        flask_login.login_user(u, remember=True)
        return flask.redirect(
            flask.request.args.get("next") or flask.url_for("main.index")
        )
    else:
        return flask.redirect(flask.url_for("main.index"))


@bp.route('/submit', methods=['GET', 'POST'])
@flask_login.login_required
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
@flask_login.login_required
def all():
    """Show all the quotes we have in our database.
    """
    quotes = [quote_to_dict(q) for q in db.list_all_quotes()]
    return flask.render_template('author.html', quotes=quotes)


@bp.route('/author/<authorName>')
@flask_login.login_required
def author(authorName):
    quotes = [quote_to_dict(q) for q in db.find_quotes_by_author(authorName)]
    return flask.render_template('author.html', quotes=quotes)


@bp.route('/admin')
@flask_login.login_required
def admin():
    """Admin dashboard for editing authors and quotes.
    TODO: Finish this.
    """
    data = {
        'usersSinceRestart': len(auth.usersSinceRestart)
        # 'quotes': db.list_all_quotes(),
        # 'authors': db.list_authors()
    }
    return flask.render_template('admin.html', data=data)
