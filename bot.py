import logging

import sqlite3

import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

import config

#****************PASSWORD GENERATOR*******************
pas = ""
for i in range(10):
    pas = pas + random.choice(list('1234567890'))
pas1 = ""
for i in range(10):
    pas1 = pas1 + random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
pas2 = ""
for i in range(10):
    pas2 = pas2 + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

#****************PASSWORD GENERATOR*******************

TOKEN = (config.token)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER
    )""")
    connect.commit()
    
    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
    data = cursor.fetchone()
    
    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()
    else:
        pass
    
    await message.reply("Hey!\nLet's start creating passwords!\nUse the /password command to create password.")

buttons = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Numbers🔢", callback_data="numbers"),
                                                InlineKeyboardButton(text="Letters🔠", callback_data="letters"),
                                                InlineKeyboardButton(text="Numbers and Letters🔡🔢", callback_data="numbersandletters"))

@dp.message_handler(commands=['password'])
async def password(message):
    await message.answer("Shall we use numbers and letters?", reply_markup=buttons)

@dp.callback_query_handler(text="numbers")
async def nums_callback(callback: types.CallbackQuery):
    await callback.message.answer(text="Ok. Your generated password is:")
    await callback.message.answer(pas)

@dp.callback_query_handler(text="letters")
async def nums_callback(callback: types.CallbackQuery):
    await callback.message.answer(text="Ok. Your generated password is:")
    await callback.message.answer(pas1)

@dp.callback_query_handler(text="numbersandletters")
async def nums_callback(callback: types.CallbackQuery):
    await callback.message.answer(text="Ok. Your generated password is:")   
    await callback.message.answer(pas2)

#***********DO NOT USE************
"""@dp.message_handler()
async def final_password_nums(message: types.Message):
    await message.answer("Your generated password is: ")
    await message.answer(pas)

dp.message_handler()
async def final_password_letters(message: types.Message):
    await message.answer("Your generated password is: ")
    await message.answer(pas1)
    

dp.message_handler()
async def final_password_numsandletters(message: types.Message):
    await message.answer("Your generated password is: ")
    await message.answer(pas2)"""
#***********DO NOT USE************    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

