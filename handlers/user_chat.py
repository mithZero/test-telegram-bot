import datetime
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import CommandStart

import datetime
from keyboards import reply 
from google_sheet_api import sheet

user_chat_router = Router()

@user_chat_router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer("Привет)",
                         reply_markup=reply.main.as_markup())
    

@user_chat_router.message()
async def date(message: Message):
    try:
        datetime.datetime.strptime(message.text, "%d.%m.%Y")
        next_row = len(sheet.sheet1.col_values(2)) + 1
        sheet.sheet1.update_cell(next_row, 2, message.text)
        await message.answer("Дата верна!")
    except ValueError:
        await message.answer("Дата неверна. Пожалуйста, введите дату в формате 'дд.мм.гггг'")


@user_chat_router.callback_query(F.data == "image")
async def send_image(callback: CallbackQuery):
    await callback.answer("Шас")

    img = FSInputFile("img1.jpg")
    await callback.bot.send_photo(callback.message.chat.id, img, caption="Ваш текст")
    # await callback.message.answer_photo(photo="https://th.bing.com/th/id/R.fc9ff391e0b92927fc4a526a939b2ca3?rik=M35YB1MrloATrw&riu=http%3a%2f%2fupload.wikimedia.org%2fwikipedia%2fcommons%2fd%2fd4%2fCat_March_2010-1a.jpg&ehk=lmx5Dow%2btE7KUtrgWeamODrZNBeLisLC4x4%2bkXQRDq8%3d&risl=1&pid=ImgRaw&r=0", caption="Просто так")


@user_chat_router.callback_query(F.data == "google")
async def send_image(callback: CallbackQuery):
    await callback.answer("Шас")

    await callback.message.answer(sheet.sheet1.acell('A2').value)