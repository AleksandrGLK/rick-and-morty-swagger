import json

from aiohttp.abc import Application
from aiohttp.web_exceptions import HTTPUnprocessableEntity
from aiohttp.web_middlewares import middleware
from aiohttp.web_response import json_response
from aiohttp_apispec import validation_middleware
from marshmallow import ValidationError


@middleware
async def error_handling_middleware(request, handler):
    try:
        return await handler(request)
    except HTTPUnprocessableEntity as e:
        return json_response(
            status=400,
            data=json.loads(e.text),
        )


def setup_middlewares(app: Application):
    app.middlewares.append(error_handling_middleware)
    app.middlewares.append(validation_middleware)
