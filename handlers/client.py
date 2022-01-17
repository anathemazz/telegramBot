from aiogram import types, Dispatcher
from createBot import dp
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

# @dp.message_handler(commands = ['start'])
async def command_start(message : types.Message):
    await message.answer('Добро пожаловать в игру "Тайный Санта"!', reply_markup = kb_client)

# @dp.message_handler(commands = ['Узнать_правила'])
async def games_rules(message : types.Message):
    await bot.send_message(message.chat.id, 'Правила игры')

# @dp.message_handler(commands = ['Принять_участие'])
async def take_part(message : types.Message):
    await bot.send_message(message.chat.id, 'Вы стали участником игры')

# @dp.message_handler(commands = ['Выйти_из_игры'])
async def leave_game(message : types.Message):
    await bot.send_message(message.chat.id, 'Вы покинули игру')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands = ['start'])
    dp.register_message_handler(games_rules, commands = ['Правила_игры'])
    dp.register_message_handler(take_part, commands = ['Принять_участие'])
    dp.register_message_handler(leave_game, commands = ['Выйти_из_игры'])