import pytest
import constants
from random import choice
from string import ascii_lowercase
from endpoints.new_url import PostNewUrl


@pytest.fixture(scope='function')
def random_url():
    random_str = ''.join(choice(ascii_lowercase) for _ in range(10))
    return f'{constants.RANDOM_URL_BASE}/{random_str}'


@pytest.fixture(scope='function')
def random_custom_short_code():
    return ''.join(choice(ascii_lowercase) for _ in range(10))


@pytest.fixture(scope='function')
def create_short_url(random_url) -> PostNewUrl:
    new_url = PostNewUrl(random_url)
    new_url.shorten()
    return new_url
