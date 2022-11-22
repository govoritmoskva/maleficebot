#Importing Aiogram, SQLite and random modules
import requests

import logging

import random
from random import randint

import sqlite3

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

#****************COIN GENERATOR***********************
coinlist = ''
coin = randint(1, 2)
if coin == 1:
    coinlist = "Орёл / Eagle"
if coin == 2:
    coinlist = "Решка / Tails"

#****************COIN GENERATOR***********************


#Giving a token and initializing bot and dispatcher

TOKEN = (config.token)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#/start command (creating a table and replying to message)

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
    
    await message.reply("Hey!💥\nThis's the fun bot created by vstyoma.\n\nList of commands: \n/password - the bot generating a random password. \n/coin - the bot randomly choice eagle or tails \n/valutes - the bot shows the desired valute ")

#Creating buttons with callback_data

buttons = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Numbers🔢", callback_data="numbers"),
                                                InlineKeyboardButton(text="Letters🔠", callback_data="letters"),
                                                InlineKeyboardButton(text="Numbers and Letters🔡🔢", callback_data="numbersandletters"))

#/password command using buttons and replies (also answering to message with generated password) 

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



@dp.message_handler(commands=['coin'])
async def welcome(message):
    await message.answer(text="Your coin is:")
    await message.answer(coinlist)

valutesbuttons = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="USD", callback_data="usdvalute"),
                                                InlineKeyboardButton(text="EUR", callback_data="eurvalute"),
                                                InlineKeyboardButton(text="KZT", callback_data="kztvalute"))

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    
USD = (data['Valute']['USD']['Value'])
EUR = (data['Valute']['EUR']['Value'])
KZT = (data['Valute']['KZT']['Value'])

@dp.message_handler(commands="valutes")
async def print_valutes(message):
    await message.answer("Select the valute you would like to see:", reply_markup=valutesbuttons)

@dp.callback_query_handler(text="usdvalute")
async def nums_callback(callback: types.CallbackQuery):
    await callback.message.answer(text="Today's price in USD is:")
    await callback.message.answer(USD)

@dp.callback_query_handler(text="eurvalute")
async def nums_callback(callback: types.CallbackQuery):
    await callback.message.answer(text="Today's price in EUR is:")
    await callback.message.answer(EUR)

@dp.callback_query_handler(text="kztvalute")
async def nums_callback(callback: types.CallbackQuery):
    await callback.message.answer(text="Today's price in KZT is:")
    await callback.message.answer(KZT)

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

#Starting our bot

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

