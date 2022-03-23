import pytest

from tests.fixtures.clone_server import list_character_original_response, get_character_original_response, \
    list_episode_original_response, get_episode_original_response, mock_rick_and_morty_api_call


class TestApp:
    @pytest.mark.parametrize(
        'path,original_data',
        [
            ('/character', list_character_original_response()),
            ('/episode', list_episode_original_response()),
        ])
    async def test_list_schema_including(self, clone_cli, path, original_data):
        resp = await clone_cli.get(path)
        assert resp.status == 200, f'Получен неуспешный ({resp.status}) статус ответа. ' \
                                   f'Скорее всего не все поля в querystring_schema помечены как необязательные'
        data = await resp.json()
        assert data == original_data, f'Данные, полученные от стороннего API и данные полученные от нашего API' \
                                      f' не совпадают. Скорее всего схема для {path} написана неверно'

    @pytest.mark.parametrize(
        'path,original_data',
        [
            ('/character/1', get_character_original_response()),
            ('/episode/1', get_episode_original_response()),
        ])
    async def test_get_schema_including(self, clone_cli, path, original_data):
        resp = await clone_cli.get(path)
        assert resp.status == 200, f'Получен неуспешный ({resp.status}) статус ответа'
        data = await resp.json()
        assert data == original_data, f'Данные, полученные от стороннего API и данные полученные от нашего API' \
                                      f' не совпадают. Скорее всего схема для {path} написана неверно'

    @pytest.mark.parametrize('path', ['/character', '/character/1', '/episode', '/episode/1'])
    async def test_schema_excluding(self, clone_cli, path):
        async def call(m, p, q):
            return {'extra': 'super_extra'}

        mock_rick_and_morty_api_call(call)
        resp = await clone_cli.get(path)
        assert resp.status == 200, f'Получен неуспешный ({resp.status}) статус ответа'
        data = await resp.json()
        assert data == {}, f'Получены лишние данные для {path}. Скорее всего не была задана response_schema'

    async def test_gender_validation(self, clone_cli):
        resp = await clone_cli.get('/character', params={
            'gender': 'bender',
        })
        assert resp.status == 400, f'Неверный статус ответа ({resp.status}). ' \
                                   f'Скорее всего не задана валидация для поля gender для списка персонажей'

    async def test_swagger_ui(self, clone_cli):
        resp = await clone_cli.get('/swagger')
        assert resp.status == 200, f'Неверный статус ответа ({resp.status}) для Swagger UI. ' \
                                   f'Скорее всего не была произведена настройка или путь указан неверно'
        assert 'text/html' in resp.headers['Content-Type'], f'Неверный тип отданных Swagger данных. ' \
                                                            f'Скорее всего перепутаны пути для json и ui Swagger\'а'

    async def test_swagger_json(self, clone_cli):
        resp = await clone_cli.get('/swagger.json')
        assert resp.status == 200, f'Неверный статус ответа ({resp.status}) для получения Swagger в формате json. ' \
                                   f'Скорее всего не была произведена настройка или путь указан неверно'
        assert 'application/json' in resp.headers['Content-Type'], \
            f'Неверный тип отданных Swagger данных. Скорее всего перепутаны пути для json и ui Swagger\'а'
