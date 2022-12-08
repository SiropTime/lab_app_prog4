import aiogram.types

from internal.telegram.utils.buttons import categories_buttons, pagination_buttons

categories_kb = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
categories_kb.add(*categories_buttons)

pagination_kb = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
categories_kb.add(*pagination_buttons)
