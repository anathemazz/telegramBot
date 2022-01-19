import requests
import json
import jwt
from email import message
from aiogram import types, Dispatcher
from createBot import dp, bot, webhook_url, rules_file
from keyboards import kb_start, kb_delete
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

def get_token(r, type_ans):
    #r = requests.post(webhook_url + '/api/user/login', data=json.dumps(dict(data)), headers={'Content-Type': 'application/json'})
    r_dict = dict(r.json())
    if (type_ans == 'token'):
        return 'Bearer ' + r_dict['token']
    elif (type_ans == 'id'):
        id_dict = jwt.decode(r_dict['token'], options={"verify_signature": False})
        return id_dict['id']
    return

#Машина состояний регистрации участника
class FSMReg(StatesGroup):
    email = State()
    password = State()
    name = State()
    age = State()
    post_adr = State()

#Начало диалога
async def cm_start(message : types.Message):
    await FSMReg.next()
    await message.reply('Введите email')

#Хендлеры отмены
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Вы передумали совершать данное действие')

#Ловим первый ответ и пишем в словарь
async def load_email(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    await FSMReg.next()
    await message.reply('Введите пароль')

#Ловим второй ответ и пишем в словарь
async def load_password(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text

    async with state.proxy() as data:
        r = requests.post(webhook_url + '/api/user/registration', data=json.dumps(dict(data)), headers={'Content-Type': 'application/json'})
        if r.status_code == 200:
            await bot.send_message(message.chat.id, 'Поздравляем! Вы стали участником игры!', reply_markup = kb_delete)
        else:
            r = requests.post(webhook_url + '/api/user/login', data=json.dumps(dict(data)), headers={'Content-Type': 'application/json'})
            if r.status_code == 200:
                await bot.send_message(message.chat.id, 'Вы уже зарегистрированы', reply_markup = kb_delete)
            else:
                await bot.send_message(message.chat.id, 'Некорректный пароль или данного участника невозможно зарегистрировать')
    await state.finish()

#Машина состояний обновления анкеты
class FSMUpdate(StatesGroup):
    email = State()
    password = State()
    name = State()
    age = State()
    post_adr = State()

#Начало диалога
async def cm_update(message : types.Message):
    await FSMUpdate.next()
    await message.reply('Введите email')

#Ловим первый ответ и пишем в словарь
async def update_email(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    await FSMUpdate.next()
    await message.reply('Введите пароль')

#Ловим второй ответ и пишем в словарь
# async def update_password(message : types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['password'] = message.text
#     async with state.proxy() as data:
#         r = requests.post(webhook_url + '/api/user/login', data=json.dumps(dict(data)), headers={'Content-Type': 'application/json'})
#         if r.status_code == 200:
#             await bot.send_message(message.chat.id, 'Вы уже зарегистрированы', reply_markup = kb_delete)
#             await FSMUpdate.next()
#             await message.reply('Введите имя')
#         else:
#             await bot.send_message(message.chat.id, 'Некорректный email или пароль')
#             await state.finish()
async def update_password(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text
    await FSMUpdate.next()
    await message.reply('Введите имя')
    

#Ловим третий ответ и пишем в словарь
async def update_name(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMUpdate.next()
    await message.reply('Введите ваш возраст')

#Ловим четвертый ответ и пишем в словарь
async def update_age(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await FSMUpdate.next()
    await message.reply('Введите адрес, на который вам прислать подарок')

#Ловим пятый ответ и пишем в словарь
async def update_post_adr(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post_adr'] = message.text

    async with state.proxy() as data:
        r = requests.post(webhook_url + '/api/user/login', data=json.dumps(dict(data)), headers={'Content-Type': 'application/json'})
        token = get_token(r, 'token')
        id = get_token(r, 'id')
        r = requests.put(webhook_url + '/api/user/' + str(id), data=json.dumps(dict(data)), headers={'Content-Type': 'application/json', 'Authorization' : token})
        if r.status_code == 200:
            await bot.send_message(message.chat.id, 'Информация успешно изменена')
        else:
            await bot.send_message(message.chat.id, 'Не удалось изменить информацию. Возможно, введен неверный пароль')
    await state.finish()
    
#Машина состояний удаления пользователя
class FSMOut(StatesGroup):
    email = State()
    password = State()

#Начало диалога
async def cm_out(message : types.Message):
    await FSMOut.next()
    await message.reply('Введите email')

#Ловим первый ответ и пишем в словарь
async def unload_email(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    await FSMOut.next()
    await message.reply('Введите пароль')

#Ловим второй ответ и пишем в словарь
async def unload_password(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text

    async with state.proxy() as data:
        r = requests.post(webhook_url + '/api/user/login', data=json.dumps(dict(data)), headers={'Content-Type': 'application/json'})
        token = get_token(r, 'token')
        id = get_token(r, 'id')
        r = requests.delete(webhook_url + '/api/user/' + str(id), data=json.dumps(dict(data)), headers={'Content-Type': 'application/json', 'Authorization' : token})
        if r.status_code == 200:
            await bot.send_message(message.chat.id, 'Вы покинули игру. Надеемся увидеть вас снова!', reply_markup=kb_start)
        else:
            await bot.send_message(message.chat.id, 'Не удалось удалить пользователя. Возможно, введен неверный пароль.')
    await state.finish()

#Машина состояний получения адресата
class FSMSanta(StatesGroup):
    email = State()
    password = State()

#Начало диалога
async def cm_santa(message : types.Message):
    await FSMSanta.next()
    await message.reply('Введите email')

#Ловим первый ответ и пишем в словарь
async def santa_email(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    await FSMSanta.next()
    await message.reply('Введите пароль')

#Ловим второй ответ и пишем в словарь
async def santa_password(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text

    async with state.proxy() as data:
        r = requests.post(webhook_url + '/api/user/login', data=json.dumps(dict(data)), headers={'Content-Type': 'application/json'})
        token = get_token(r, 'token')
        id = get_token(r, 'id')
        r = requests.get(webhook_url + '/api/userPair/' + str(id), data=json.dumps(dict(data)), headers={'Content-Type': 'application/json', 'Authorization' : token})
        if r.status_code == 200:
            await bot.send_message(message.chat.id, r.json())
        else:
            await bot.send_message(message.chat.id, 'Адресат пока не назначен')
    await state.finish()


# @dp.message_handler(commands = ['start'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать в игру "Тайный Санта"!', reply_markup = kb_start)

# @dp.message_handler(commands = ['Правила_игры'])
async def games_rules(message : types.Message):
    await bot.send_message(message.chat.id, rules_file.read())

# @dp.message_handler(commands = ['Перейти_на_сайт'])
async def go_to_site(message : types.Message):
    await bot.send_message(message.chat.id, 'http://localhost:3000/home')


#@dp.message_handler()
async def empty(message: types.Message):
    await message.answer('Стать Сантой гораздо лучше, чем болтать о пустяках=)')
    await message.delete()


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands = ['start'])
    dp.register_message_handler(games_rules, commands = ['Правила_игры'])
    dp.register_message_handler(go_to_site, commands = ['Перейти_на_сайт'])
    dp.register_message_handler(cm_start, commands = ['Стать_Сантой'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_email, state=FSMReg.email)
    dp.register_message_handler(load_password,state=FSMReg.password)
    dp.register_message_handler(cm_update, commands = ['Обновить_анкету'], state=None)
    dp.register_message_handler(update_email, state=FSMUpdate.email)
    dp.register_message_handler(update_password,state=FSMUpdate.password)
    dp.register_message_handler(update_name, state=FSMUpdate.name)
    dp.register_message_handler(update_age, state=FSMUpdate.age)
    dp.register_message_handler(update_post_adr, state=FSMUpdate.post_adr)
    dp.register_message_handler(cm_out, commands = ['Покинуть_игру'], state=None)
    dp.register_message_handler(unload_email, state=FSMOut.email)
    dp.register_message_handler(unload_password, state=FSMOut.password)
    dp.register_message_handler(cm_santa, commands = ['Покинуть_игру'], state=None)
    dp.register_message_handler(santa_email, state=FSMSanta.email)
    dp.register_message_handler(santa_password, state=FSMSanta.password)
    dp.register_message_handler(empty)