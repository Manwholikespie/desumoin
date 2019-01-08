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
    return flask.render_template('submit.html')