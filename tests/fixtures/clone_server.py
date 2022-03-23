import json
import os
from typing import Union

import pytest
from aiohttp.test_utils import TestClient
from multidict import MultiDictProxy

from tests.fixtures import FIXTURE_PATH

from clone_server.app.base.api import RickAndMortyApi
from clone_server.main import app


@pytest.fixture(scope='session')
def clone_server():
    return app


@pytest.fixture()
def clone_cli(aiohttp_client, loop, clone_server) -> TestClient:
    return loop.run_until_complete(aiohttp_client(clone_server))


def list_character_original_response():
    with open(os.path.join(FIXTURE_PATH, 'mocks', 'rick_and_morty', 'list_character.json')) as f:
        data = json.load(f)
    return data


def get_character_original_response():
    with open(os.path.join(FIXTURE_PATH, 'mocks', 'rick_and_morty', 'get_character.json')) as f:
        data = json.load(f)
    return data


def list_episode_original_response():
    with open(os.path.join(FIXTURE_PATH, 'mocks', 'rick_and_morty', 'list_episode.json')) as f:
        data = json.load(f)
    return data


def get_episode_original_response():
    with open(os.path.join(FIXTURE_PATH, 'mocks', 'rick_and_morty', 'get_episode.json')) as f:
        data = json.load(f)
    return data


@pytest.fixture(autouse=True)
def clone_mocker():
    async def call(method: str, path: str, query_params: Union[dict, MultiDictProxy]) -> dict:
        if path == '/character':
            return list_character_original_response()
        elif path.startswith('/character'):
            return get_character_original_response()
        elif path == '/episode':
            return list_episode_original_response()
        elif path.startswith('/episode'):
            return get_episode_original_response()
        else:
            raise NotImplementedError

    RickAndMortyApi.call = call


def mock_rick_and_morty_api_call(mock_func):
    RickAndMortyApi.call = mock_func
