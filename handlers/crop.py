from aiogram import types
from main import dp
from aiogram.dispatcher.filters import Command
from states import Crop
from PIL import Image
from aiogram.dispatcher.storage import FSMContext

def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
    
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) / 2,
                         (img_height - crop_height) / 2,
                         (img_width + crop_width) / 2,
                         (img_height + crop_height) / 2))

@dp.message_handler(Command("crop"))
async def crop(message: types.Message):
    await message.answer("Отправте мне фото которое хотите обрезать:")

    await Crop.imgsource.set()

@dp.message_handler(content_types=['photo'], state=Crop.imgsource)
async def imgcrop(message: types.Message, state: FSMContext):
    await state.update_data(photo_id=message.photo[-1].photo_id)

    await message.answer("Введите высоту для обрезки в пикселях:")

    await Crop.width.set()

@dp.message_handler(state=Crop.width)
async def width(message: types.Message, state: FSMContext):
    width = int(message.text)

    await state.update_data(width=width)

    await message.answer("Введите ширину для обрезки в пикселях:")

    await Crop.height.set()

@dp.message_handler(state=Crop.height)
async def height(message: types.Message, state: FSMContext):
    height = int(message.text)

    await state.update_data(height=height)

    data = await state.get_data()
    width = data.get("width")
    height = data.get("height")
    photo_id = data.get("photo_id")

    await message.answer(f"{width}\n{height}")

    await bot.download_file_by_id(photo_id, f'{photo_id}.png')

    im = Image.open(f'{photo_id}.png')
    im_new = crop_center(im, height, width)
    im_new.save(f'{photo_id}_crop.png', quality=95)

    crop = open(f'{photo_id}_crop.png', 'rb')

    await message.answer(f"Держите результат:")
    await message.answer_photo(crop)

    await state.finish()

    

