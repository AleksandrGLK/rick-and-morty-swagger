from typing import Union

import aiohttp
from multidict import MultiDictProxy

BASE_PATH = "https://rickandmortyapi.com/api"


class RickAndMortyApi:
    @staticmethod
    async def call(
        method: str, path: str, query_params: Union[dict, MultiDictProxy]
    ) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method, f'{BASE_PATH}/{path.strip("/")}', params=dict(query_params)
            ) as resp:
                res = await resp.json()
                return res
