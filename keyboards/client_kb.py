from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Узнать_правила')
b2 = KeyboardButton('/Принять_участие')
b3 = KeyboardButton('/Выйти_из_игры')

kb_client = ReplyKeyboardMarkup()

kb_client.add(b1).add(b2).add(b3)