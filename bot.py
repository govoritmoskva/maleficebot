import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import config

TOKEN = (config.token)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message):
    await message.reply("Hey!\nLet's start creating passwords!\nUse the /password command to create password.")

buttons = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Numbers", callback_data="numbers"),
                                                InlineKeyboardButton(text="Letters", callback_data="letters"),
                                                InlineKeyboardButton(text="Numbers and Letters", callback_data="numbersandletters"))

@dp.message_handler(commands=['password'])
async def password(message):
  
   
   
   
    
    await message.answer("Shall we use numbers and letters?", reply_markup=buttons)

@dp.callback_query_handler(text="numbers")
async def nums_callback(callback: types.CallbackQuery):
    await callback.message.answer(text="Ok. Enter the number of characters from 1 to 16")
@dp.callback_query_handler(text="letters")
async def nums_callback(callback: types.CallbackQuery):
    await callback.message.answer(text="Ok. Enter the number of characters from 1 to 16")
@dp.callback_query_handler(text="numbersandletters")
async def nums_callback(callback: types.CallbackQuery):
    await callback.message.answer(text="Ok. Enter the number of characters from 1 to 16")   


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

