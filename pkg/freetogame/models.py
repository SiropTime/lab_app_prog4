from pydantic import BaseModel


class GameModel(BaseModel):
    id: int
    title: str
    thumbnail: str  # ULR for image
    short_description: str
    game_url: str
    genre: str
    platform: str
    publisher: str
    developer: str
    release_date: str
    freetogame_profile_url: str


class GamesResponseModel(BaseModel):
    games: list[GameModel]

