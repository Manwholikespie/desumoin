import flask_login

from src.models import User

auth_manager = flask_login.LoginManager()

usersSinceRestart = set([])

@auth_manager.user_loader
def load_user(userId):
    if userId in usersSinceRestart:
        return User(userId)
    return None

def add_user(userId):
    usersSinceRestart.add(userId)