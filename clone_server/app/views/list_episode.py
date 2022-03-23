from clone_server.app.base.view import View
from aiohttp_apispec import docs, response_schema, querystring_schema

from clone_server.app.schemas import ListEpisodeRequestSchema, ListEpisodeResponseSchema


class ListEpisodeView(View):
    @docs(tags=["Episode"], summary="Get List of Episodes")
    @querystring_schema(ListEpisodeRequestSchema)
    @response_schema(ListEpisodeResponseSchema)
    async def get(self):
        return await super().get()
