from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

color = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="black"),
            KeyboardButton(text="white"),
            KeyboardButton(text="gray"),
        ],
        [
            KeyboardButton(text="gray"),
            KeyboardButton(text="pink"),
            KeyboardButton(text="violet"),
        ],
        [
            KeyboardButton(text="red"),
            KeyboardButton(text="blue"),
            KeyboardButton(text="yellow"),
        ],
    ],
    resize_keyboard=True
)