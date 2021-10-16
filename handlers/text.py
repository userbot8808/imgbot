from aiogram.dispatcher.storage import FSMContext
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from keyboards import color
from main import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from states import Img
from PIL import Image, ImageFont, ImageDraw
import textwrap

def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
    
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) / 2,
                         (img_height - crop_height) / 2,
                         (img_width + crop_width) / 2,
                         (img_height + crop_height) / 2))

@dp.message_handler(Command("text"))
async def question1(message: types.Message):
    await message.answer("Отправте фото:")

    await Img.img.set()

@dp.message_handler(content_types=['photo'], state=Img.img)
async def img(message: types.Message):
    await message.photo[-1].download('source.png')

    im = Image.open('source.png')
    im_new = crop_center(im, 500, 500)
    im_new.save('img.png')

    await message.answer("Введите цвет текста\(\#000000, \#ffffff и так далее\):", reply_markup=color)

    await Img.color.set()

@dp.message_handler(state=Img.color)
async def img(message: types.Message, state: FSMContext):

    color = message.text

    await state.update_data(color=color)

    await message.answer("Введите размер текста до 200:", reply_markup=ReplyKeyboardRemove())
    fontimg = open('img.png', 'rb')
    await message.answer_photo(fontimg)

    await Img.font.set()

@dp.message_handler(state=Img.font)
async def img(message: types.Message, state: FSMContext):

    font = int(message.text)

    if (201 > font):
        await state.update_data(font=font)

        await message.answer("Введите текст:")

        await Img.text.set()
    else:
        await message.answer("Я ж сказал, НЕ БОЛЬШЕ 200!!!, клоун рил")
        await Img.font.set()

@dp.message_handler(state=Img.text)
async def text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    color = data.get("color")
    font = data.get("font")
    text = message.text
    width = 15
    text1 = textwrap.fill(text, width)
    photo = Image.open('img.png')
    draw = ImageDraw.Draw(photo)
    fontg = ImageFont.truetype("arial.ttf", size=font)
    w, h = draw.textsize(text1, font=fontg)
    W, H = (500, 500)
    draw.text(((W-w)/2, (H-h)/2), text1, font=fontg, fill=f"{color}")
    photo.save('img1.png', "PNG")
    finish = open('img1.png', 'rb')

    await message.answer_photo(finish)

    await state.finish()
