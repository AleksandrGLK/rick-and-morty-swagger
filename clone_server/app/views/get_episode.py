from clone_server.app.base.view import View
from aiohttp_apispec import docs, response_schema

from clone_server.app.schemas import EpisodeSchema


class GetEpisodeView(View):
    @docs(tags=["Episode"], summary="Get Episode")
    @response_schema(EpisodeSchema)
    async def get(self):
        return await super().get()
