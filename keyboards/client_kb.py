from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


b1 = InlineKeyboardButton(text='/Правила_игры', callback_data="/Правила_игры")
b2 = InlineKeyboardButton(text='/Стать_Сантой', callback_data="/Правила_игры")
b3 = InlineKeyboardButton(text='/Перейти_на_сайт', callback_data="/Правила_игры")

# kb_client = InlineKeyboardMarkup(resize_keyboard = True)
kb_client = InlineKeyboardMarkup(row_width=3)

kb_client.add(b1).add(b2).add(b3)