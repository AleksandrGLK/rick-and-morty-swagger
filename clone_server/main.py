from aiohttp import web
from aiohttp_apispec import setup_aiohttp_apispec

from clone_server.app.middlewares import setup_middlewares
from clone_server.app.routes import setup_routes


def create_and_setup_app() -> web.Application:
    app = web.Application()
    setup_routes(app)
    setup_aiohttp_apispec(
        app,
        title="Rick and Morty API-clone documentation",
        url="/swagger.json",
        swagger_path="/swagger",
    )
    setup_middlewares(app)
    return app


app = create_and_setup_app()

if __name__ == "__main__":
    web.run_app(app)
