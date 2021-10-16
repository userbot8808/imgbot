from aiogram.dispatcher.filters.state import StatesGroup, State

class Img(StatesGroup):
    img = State()
    color = State()
    font = State()
    text = State()