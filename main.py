import asyncio
import logging
# import os

from aiogram import Bot, types, Dispatcher
from aiogram.filters import CommandStart
from beast import Beastiary


# TOKEN = os.getenv('TOKEN')
TOKEN = open('token.txt').read()
bot = Bot(token=TOKEN)
dp = Dispatcher()
chats = {}


@dp.message(CommandStart())
async def send_welcome(msg: types.Message):
    await msg.reply(f'Я бот. Приятно познакомиться, {msg.from_user.first_name}')


@dp.message()
async def get_text_messages(msg: types.Message):
    if msg.chat.id not in chats:
        chats[msg.chat.id] = Beastiary()
    answer = chats[msg.chat.id].handle(msg)
    if answer:
        await msg.answer(answer)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.info('Service started')
    asyncio.run(main())
