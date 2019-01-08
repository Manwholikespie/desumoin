from src.views import (
    main
)

def register_views(flask_app):
    """ Attach the blueprints we have made to our flask application. """
    flask_app.register_blueprint(main.bp)

    return flask_app