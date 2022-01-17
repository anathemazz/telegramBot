from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Правила_игры')
b2 = KeyboardButton('/Стать_Сантой')
b3 = KeyboardButton('/Перейти_на_сайт')

kb_client = ReplyKeyboardMarkup(resize_keyboard = True)

kb_client.add(b1).add(b2).add(b3)