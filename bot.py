

import logging

from aiogram import Bot, Dispatcher, executor, types
import wikipedia

wikipedia.set_lang('uz')
API_TOKEN = '7641889393:AAGbKHXSOy2TwS9DKDJXfhUGD2CLPHvXFIA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    
    await message.reply("Wikipedia botiga xush kelibsiz")


@dp.message_handler()
async def cats(message: types.Message):
    try:
        resualt = wikipedia.summary(message.text)
        await message.answer(resualt)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi!!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)