from aiogram.types import BotCommand
from bot import bot, dispatcher
from sys import exit
from config import RUNNING_MODE, POSSIBLY_MODES
from handlers.mainhandlers import router as main
from handlers.cringyahhhandler import router as cringeahh

dispatcher.include_router(main)

dispatcher.include_router(cringeahh)


async def set_commands():
    await bot.set_my_commands(
        [
        BotCommand(command='/start', description='запускает ботика'),
        BotCommand(command='/info', description='инфа'),
        BotCommand(command='/help', description='зач'),
        BotCommand(command='/meme', description='очевидное'),
    ])


@dispatcher.startup()
async def uponstartup():
    await set_commands()


def run_pulling():
    dispatcher.run_polling(bot)


def run_webhook():
    pass


if __name__ == '__main__':
    if RUNNING_MODE == POSSIBLY_MODES[0]:
        run_pulling()
    elif RUNNING_MODE == POSSIBLY_MODES[1]:
        run_webhook()
    else:
        exit()
