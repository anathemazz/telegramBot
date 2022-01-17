# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram import types, Dispatcher
# from createBot import dp

# class FSMAdmin(StatesGroup):
#     email = State()
#     password = State()
#     name = State()
#     age = State()
#     post_adr = State()

# #Начало диалога
# #@dp.message_handler(commands = 'Загрузить', state = None)
# async def cm_start(message : types.Message):
#     await FSMAdmin.next()
#     await message.reply('Введите email')

# #Ловим первый ответ и пишем в словарь
# #@dp.message_handler(commands = ['email'], state = FSMAdmin.email)
# async def load_email(message : types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['email'] = message.text
#     await FSMAdmin.next()
#     await message.reply('Введите пароль')

# #Ловим второй ответ и пишем в словарь
# #@dp.message_handler(state = FSMAdmin.password)
# async def load_password(message : types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['password'] = message.text
#     await FSMAdmin.next()
#     await message.reply('Введите имя')

# #Ловим третий ответ и пишем в словарь
# #@dp.message_handler(state = FSMAdmin.name)
# async def load_name(message : types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name'] = message.text
#     await FSMAdmin.next()
#     await message.reply('Введите ваш возраст')

# #Ловим четвертый ответ и пишем в словарь
# #@dp.message_handler(state = FSMAdmin.age)
# async def load_age(message : types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['age'] = message.text
#     await FSMAdmin.next()
#     await message.reply('Введите адрес, на который вам прислать подарок')

# #Ловим пятый ответ и пишем в словарь
# #@dp.message_handler(state = FSMAdmin.post_adr)
# async def load_post_adr(message : types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['post_adr'] = message.text

#     async with state.proxy() as data:
#         await message.reply(str(data))
#     await state.finish()

# #Регистрируем хэндлеры
# def register_handlers_admin(dp : Dispatcher):
#     dp.register_message_handler(cm_start, commands = ['Загрузить'], state=None)
#     dp.register_message_handler(load_email, state=FSMAdmin.email)
#     dp.register_message_handler(load_password,state=FSMAdmin.password)
#     dp.register_message_handler(load_name, state=FSMAdmin.name)
#     dp.register_message_handler(load_age, state=FSMAdmin.age)
#     dp.register_message_handler(load_post_adr, state=FSMAdmin.post_adr)