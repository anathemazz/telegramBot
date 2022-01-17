from email import message
from aiogram import types, Dispatcher
from createBot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

class FSMAdmin(StatesGroup):
    email = State()
    password = State()
    name = State()
    age = State()
    post_adr = State()

#Начало диалога
#@dp.message_handler(commands = 'Стать_Сантой', state = None)
async def cm_start(message : types.Message):
    await FSMAdmin.next()
    await message.reply('Введите email')

#Хендлеры отмены
#@dp.message_handler(state="*", commands='отмена')
#@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')


#Ловим первый ответ и пишем в словарь
#@dp.message_handler(commands = ['email'], state = FSMAdmin.email)
async def load_email(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите пароль')

#Ловим второй ответ и пишем в словарь
#@dp.message_handler(state = FSMAdmin.password)
async def load_password(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите имя')

#Ловим третий ответ и пишем в словарь
#@dp.message_handler(state = FSMAdmin.name)
async def load_name(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите ваш возраст')

#Ловим четвертый ответ и пишем в словарь
#@dp.message_handler(state = FSMAdmin.age)
async def load_age(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите адрес, на который вам прислать подарок')

#Ловим пятый ответ и пишем в словарь
#@dp.message_handler(state = FSMAdmin.post_adr)
async def load_post_adr(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post_adr'] = message.text

    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()
    await bot.send_message(message.chat.id, 'Вы стали участником игры')

# @dp.message_handler(commands = ['start'])
async def command_start(message : types.Message):
    await message.answer('Добро пожаловать в игру "Тайный Санта"!', reply_markup = kb_client)

# @dp.message_handler(commands = ['Правила_игры'])
async def games_rules(message : types.Message):
    await bot.send_message(message.chat.id, 'Правила игры')

# # @dp.message_handler(commands = ['Стать_Сантой'])
# async def take_part(message : types.Message):
#     await bot.send_message(message.chat.id, 'Вы стали участником игры')

# @dp.message_handler(commands = ['Перейти_на_сайт'])
async def leave_game(message : types.Message):
    await bot.send_message(message.chat.id, 'Вы покинули игру')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands = ['start'])
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(games_rules, commands = ['Правила_игры'])
    #dp.register_message_handler(take_part, commands = ['Стать_Сантой'])
    dp.register_message_handler(leave_game, commands = ['Перейти_на_сайт'])
    dp.register_message_handler(cm_start, commands = ['Стать_Сантой'], state=None)
    dp.register_message_handler(load_email, state=FSMAdmin.email)
    dp.register_message_handler(load_password,state=FSMAdmin.password)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_post_adr, state=FSMAdmin.post_adr)
    