from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from bot import bot
from bot.config import BASE_DIR

router = Router()
@router.message(Command(commands=['start', 'help']))
async def route(message: Message):
    await message.answer('Здарова')

@router.message(Command(commands=['info']))
async def route1(message: Message):
    calc_info = BASE_DIR /'infonetblinblinchik/Calcblinchik.png'
    calc_info = FSInputFile(calc_info)
    await message.answer('Раздаю киндеры')
    await message.answer('Йесли ти хочешь штоб я за тебя пощитал, во те плимел: ')
    await bot.send_photo(chat_id=message.chat.id, photo=calc_info, caption=' ')

@router.message(Command(commands=['calc']))
async def calc(message: Message):
    example = message.text[5:]
    try:
        example = eval(example)
        await message.answer('вот ответка: ' + str(example))
    except Exception as e:
        print(e)
        await message.answer('Чиго налес')