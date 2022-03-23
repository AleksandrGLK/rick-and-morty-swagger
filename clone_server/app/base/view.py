from aiohttp import web
from marshmallow import Schema

from clone_server.app.base.api import RickAndMortyApi


class View(web.View):
    async def get(self):
        data = await RickAndMortyApi.call(
            self.request.method, self.request.path, self.request.query
        )
        schema: Schema = self.get.__dict__["__apispec__"]["responses"]["200"]["schema"]
        json_data = schema.dumps(data)
        return web.Response(
            body=json_data, headers={"Content-Type": "application/json"}
        )
