from src.views import (
    main, api
)

def register_views(flask_app):
    """ Attach the blueprints we have made to our flask application. """
    flask_app.register_blueprint(main.bp)
    flask_app.register_blueprint(api.bp)

    return flask_app