"""
Place classes you make here.
"""

from flask_login import UserMixin
import uuid


class User(UserMixin):
    """Our basic user class that interacts with flask-login."""

    # State enums
    STATE_UNAUTHENTICATED = 0
    STATE_AUTHENTICATED = 1

    # Default state
    state = STATE_UNAUTHENTICATED

    def __init__(self, userId=None):
        if not userId:
            self.id = uuid.uuid4()
        else:
            self.id = userId
    
    def verify_credentials(self, credentials, properCredentials):
        if credentials == properCredentials:
            self.state = self.STATE_AUTHENTICATED

    def is_authenticated(self):
        """
        Returns
        -------
        bool : True if user is authenticated.
        """
        return self.state == self.STATE_AUTHENTICATED
    
    def get_id(self):
        """
        Returns
        -------
        str : Uniquely identifies this user, and can be used to load the user
              from the user_loader callback.
        """
        return self.id