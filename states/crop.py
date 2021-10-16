from aiogram.dispatcher.filters.state import StatesGroup, State

class Crop(StatesGroup):
    imgsource = State()
    width = State()
    height = State()
    result = State()