from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

webhook_url = 'https://5623-46-173-42-227.eu.ngrok.io'
rules_file = open('SecretSanta.txt', "r", encoding="utf-8")

storage = MemoryStorage()

bot = Bot(token = os.getenv('TOKEN'))
dp = Dispatcher(bot, storage = storage)