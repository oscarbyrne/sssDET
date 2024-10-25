import yaml
from pathlib import Path


class User:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def from_yaml(cls, path):
        return [
            cls(user['email'], user['password'])
            for user in yaml.safe_load(Path(path).read_text())
        ]

    def __repr__(self):
        return f'User(email="{self.email}", password="{self.password}")'
