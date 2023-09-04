from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/PizzaKsenonBot')

# @dp.message_handler(commands=['График'])
async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Каждый день с 9 до 22')

# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'ул. Северная  59')


@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message : types.Message):
	await sqlite_db.sql_read(message)
 	

def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start', 'help'])
	dp.register_message_handler(pizza_open_command, commands=['График'])
	dp.register_message_handler(pizza_place_command, commands=['Расположение'])
	dp.register_message_handler(pizza_menu_command, commands=['Меню'])