import requests

from .constants import API_URL
from .models import GameModel


def get_games_by_request(path: str, **kwargs) -> list[GameModel]:
    r = requests.get(f"{API_URL}{path}"
                     f"{'&'.join([f'{k}={v}' for k, v in kwargs])}")
    if r.status_code == 404:
        raise Exception("Can't find this endpoint or game")
    response_body = r.json()

    response_array = list[GameModel]()

    for g in response_body:
        game = GameModel(**g)
        response_array.append(game)

    return response_array
