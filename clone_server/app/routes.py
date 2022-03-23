from clone_server.app.views.get_character import GetCharacterView
from clone_server.app.views.get_episode import GetEpisodeView
from clone_server.app.views.list_character import ListCharacterView
from clone_server.app.views.list_episode import ListEpisodeView


def setup_routes(app):
    app.router.add_view("/character", ListCharacterView)
    app.router.add_view("/character/{id}", GetCharacterView)
    app.router.add_view("/episode", ListEpisodeView)
    app.router.add_view("/episode/{id}", GetEpisodeView)
