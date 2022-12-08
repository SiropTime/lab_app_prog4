from aiogram.dispatcher.filters.state import StatesGroup, State


class SearchStates(StatesGroup):
    query = State()
    pagination = State()


class MovieReviewsStates(StatesGroup):
    query = State()
