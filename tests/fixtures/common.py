import os

import pytest
from aiohttp.test_utils import loop_context

FIXTURE_PATH = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture(scope="session")
def loop():
    with loop_context() as _loop:
        yield _loop
