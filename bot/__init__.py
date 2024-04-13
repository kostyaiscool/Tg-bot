from aiogram import Bot, Dispatcher
from os import getenv


TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN', '7153356607:AAGs4Jh737Pz0-HduR-jZ_d-UXE3nCppA2Q')
bot = Bot(TELEGRAM_TOKEN)
dispatcher = Dispatcher()
