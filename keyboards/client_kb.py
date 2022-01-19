from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Правила_игры')
b2 = KeyboardButton('/Стать_Сантой')
b3 = KeyboardButton('/Обновить_анкету')
b4 = KeyboardButton('/Покинуть_игру')
b5 = KeyboardButton('/Перейти_на_сайт')
b6 = KeyboardButton('/Для_кого_я_Санта')

kb_start = ReplyKeyboardMarkup(resize_keyboard = True)
kb_delete = ReplyKeyboardMarkup(resize_keyboard = True)

kb_start.add(b1).add(b2).add(b5)
kb_delete.add(b1).add(b3).insert(b4).add(b6).add(b5)