from clone_server.app.base.view import View
from aiohttp_apispec import docs, response_schema, querystring_schema

from clone_server.app.schemas import (
    ListCharacterRequestSchema,
    ListCharacterResponseSchema,
)


class ListCharacterView(View):
    @docs(tags=["Character"], summary="Get List of Characters")
    @querystring_schema(ListCharacterRequestSchema)
    @response_schema(ListCharacterResponseSchema)
    async def get(self):
        return await super().get()
