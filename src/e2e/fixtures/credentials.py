import pytest

from data.factory import Static


@pytest.fixture
def data():
    return Static()

@pytest.fixture
def user_with_email(data):
    return data.user_with_email
