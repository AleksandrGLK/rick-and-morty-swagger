from clone_server.app.base.view import View
from aiohttp_apispec import docs, response_schema

from clone_server.app.schemas import CharacterSchema


class GetCharacterView(View):
    @docs(tags=["Character"], summary="Get Character")
    @response_schema(CharacterSchema)
    async def get(self):
        return await super().get()
