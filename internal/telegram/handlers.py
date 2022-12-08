import time

import aiogram.types

from internal.telegram.utils.buttons import categories_buttons, pagination_buttons
from internal.telegram.utils.keyboards import categories_kb, pagination_kb
from internal.utils import WELCOME_MESSAGE

from main import dp

from .usecase import return_all_books, find_articles, find_popular_articles, find_movie_reviews
from .utils.states import SearchStates, MovieReviewsStates

from aiogram import types


async def send_menu(message: types.Message):
    await message.answer(WELCOME_MESSAGE, reply_markup=categories_kb)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):

    await message.answer(WELCOME_MESSAGE,
                         reply_markup=categories_kb)


@dp.message_handler(lambda msg: msg.text == categories_buttons[0])  # msg.text == "Последние бестселлеры"
async def all_books(message: types.Message):
    await message.answer("Последние бестселлеры")
    books = return_all_books()
    for book in books:
        await message.answer(book, parse_mode=aiogram.types.ParseMode.MARKDOWN)
        time.sleep(1)


@dp.message_handler(lambda msg: msg.text == categories_buttons[1])
async def find_article(message: types.Message):
    await message.answer("Введите запрос (на английском языке):", reply_markup=None)
    await SearchStates.query.set()


@dp.message_handler(lambda msg: msg.text == categories_buttons[2])
async def popular_articles(message: types.Message):
    await message.answer("Популярные статьи")
    articles = find_popular_articles()
    for article in articles:
        await message.answer(article, parse_mode=aiogram.types.ParseMode.MARKDOWN)
        time.sleep(1)


@dp.message_handler(lambda msg: msg.text == categories_buttons[3])
async def movie_reviews(message: types.Message):
    await message.answer("Введите запрос для поиска рецензий:")
    await MovieReviewsStates.query.set()


@dp.message_handler(state=MovieReviewsStates.query)
async def process_query(message: types.Message, state: aiogram.dispatcher.FSMContext):
    query = message.text
    reviews = find_movie_reviews(query)
    for review in reviews:
        await message.answer(review, parse_mode=aiogram.types.ParseMode.MARKDOWN)
        time.sleep(1)
    await state.finish()
    await send_menu(message)


@dp.message_handler(state=SearchStates.query)
async def process_query(message: types.Message, state: aiogram.dispatcher.FSMContext):
    query = message.text
    await message.answer(f"Вы ищите: {query}")
    await state.update_data(query=query, page=0)

    articles = find_articles(query)
    for article in articles:
        await message.answer(article, parse_mode=aiogram.types.ParseMode.MARKDOWN)
        time.sleep(1)
    await message.reply("Хотите посмотреть дальше?", reply_markup=pagination_kb)
    await SearchStates.next()


@dp.message_handler(state=SearchStates.pagination)
async def process_pagination(message: types.Message, state: aiogram.dispatcher.FSMContext):
    query = (await state.get_data())["query"]
    page = (await state.get_data())["page"]
    if message.text == pagination_buttons[0]:
        if page == 0:
            await message.answer("Вы на первой странице")
        else:
            page -= 1
            await state.update_data(page=page)
            articles = find_articles(query, page)
            for article in articles:
                await message.answer(article, parse_mode=aiogram.types.ParseMode.MARKDOWN)
                time.sleep(1)
            await message.reply("Хотите посмотреть дальше?", reply_markup=pagination_kb)
    elif message.text == pagination_buttons[1]:
        page += 1
        await state.update_data(page=page)
        articles = find_articles(query, page)
        for article in articles:
            await message.answer(article, parse_mode=aiogram.types.ParseMode.MARKDOWN)
            time.sleep(1)
        await message.reply("Хотите посмотреть дальше?", reply_markup=pagination_kb)
    elif message.text == pagination_buttons[2]:
        await message.answer("Выход из просмотра статей")
        await state.finish()
        await send_menu(message)

    else:
        await message.answer("Нажмите на кнопку")
