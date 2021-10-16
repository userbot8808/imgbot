from aiogram import executor
from main import dp
import handlers
from commands import set_default_commands

async def on_startup(dispatcher):
    print("Бот запущен")
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)