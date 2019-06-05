import flask

import src.db as db

app = flask.current_app
bp = flask.Blueprint('api', __name__)

@bp.route('/yuri/all')
def yuri():
    """
    JSON API for Chad
    """
    # It would be pointless at this point to administer individual api keys.
    credentials = flask.request.form.get('passphrase')
    if credentials == app.config['SECRET_PASSPHRASE']:
        return flask.jsonify(db.list_all_quotes())
    else:
        return flask.Response('Una/u/thorized', 403)