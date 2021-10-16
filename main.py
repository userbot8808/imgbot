from aiogram import Bot, Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types.message import ParseMode

bot = Bot(token="2063496925:AAHXTCV2ofew-xRdKf_z8vufFTBW4cd75pY", parse_mode=ParseMode.MARKDOWN_V2)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)