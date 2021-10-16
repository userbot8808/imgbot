from main import dp
from aiogram.dispatcher.filters import Command
from aiogram import types

@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Hello {message.from_user.username}")