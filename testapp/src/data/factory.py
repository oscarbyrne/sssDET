from pathlib import Path

from .models import User


STATIC_DATA = Path(__file__).with_name('static')


def get_users(path = STATIC_DATA):
    return User.from_yaml(path / 'users.yml')
