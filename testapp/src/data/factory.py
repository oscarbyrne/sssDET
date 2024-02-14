from pathlib import Path

from data.models import User


STATIC_DIR = Path(__file__).with_name('static')


class Static:

    def __init__(self, path = STATIC_DIR):
        self.path = path

    @property
    def users_file(self):
        return self.path / 'users.yml'

    @property
    def users(self):
        return User.from_yaml(self.users_file)

    def user_with_email(self, email):
        return next(
            user for user in self.users
            if user.email == email
        )
