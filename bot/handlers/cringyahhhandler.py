from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from random import choice, randint
import os

from bot import bot
from bot.config import BASE_DIR

router = Router()
voprosiki = {'Сколько будет 2+2': '5', 'Сколько у тебя отчимов': '999'}
sloovar = dict()

@router.message(Command(commands=['meme']))
async def routecringe(message: Message):
    path_to_memes = BASE_DIR /'Мемы'
    memes_list = os.listdir(path_to_memes)
    await message.answer('Да иди на:')
    # await message.answer_photo(choice(memes_list))
    choosed_meme = path_to_memes/choice(memes_list)
    # with open(choosed_meme, 'rb') as photo:
    print(choosed_meme)
    choosed_meme = FSInputFile(choosed_meme)
    await bot.send_photo(chat_id=message.chat.id, photo=choosed_meme, caption=' ')
@router.message(Command(commands=['voprosiki']))
async def routeotchim(message: Message):
    choosed_voprosik = randint(0, len(voprosiki))
    iqnormigroka = 0
    for voprosik in voprosiki:
        if iqnormigroka == choosed_voprosik:
            vopros, answer = voprosik, voprosiki[voprosik]
            sloovar[message.from_user.id] = answer
        iqnormigroka += 1
    await message.answer('Ванечкин, ИСПОЛЬЗУЙ /answer С ОТВЕТОМ!!!!!!111111 ' + vopros)
@router.message(Command(commands=['answer']))
async def routekakuygifkutut(message:Message):
    atvet69 = message.text[7:]
    atvet69 = atvet69.replace(' ', '')
    print(atvet69, sloovar[message.from_user.id], len(atvet69), len(sloovar[message.from_user.id]))
    if atvet69 == sloovar[message.from_user.id]:
        await message.answer('чо самий умний тют столи')
    else:
        await message.answer('Выйди на улитсу и потрогай траву')