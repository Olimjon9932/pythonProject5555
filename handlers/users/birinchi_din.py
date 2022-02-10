from aiogram import types
from keyboards.default.diniy_kalima import din
from loader import dp


# Echo bot
@dp.message_handler(text="☝️OLTI DINIY KALIMA☝️")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/salom9899/232", caption="Islom dinidagi olti diniy kalima", reply_markup=din),

@dp.message_handler(text="1-Diniy kalima")
async def bot_echo(message: types.Message):
    await message.answer(text="""1. Kalimai toyyiba

La ilaha illallohu Muhammadur rosululloh.

To‘g‘ri so‘z: Allohdan o‘zga sig‘iniladigan (iloh) yo‘qdir! Muhammad Allohning rasulidir! """)