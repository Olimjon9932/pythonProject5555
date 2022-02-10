from aiogram import types
from keyboards.default.diniy_kalima import din
from loader import dp


# Echo bot
@dp.message_handler(text="☝️OLTI DINIY KALIMA☝️")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/salom9899/232", caption="Islom dinidagi olti diniy kalima", reply_markup=din),

@dp.message_handler(text="2-Diniy kalima")
async def bot_echo(message: types.Message):
    await message.answer(text="""2. Kalimai shahodat

Ashhadu alla ilaha illallohu va ashhadu anna Muhammadan ‘abduhu va rosuluh.

Iqrorlik so‘zi: Allohdan o‘zga sig‘iniladigan (iloh)ning yo‘qligiga va Muhammad Allohning bandasi va rasuli ekaniga iqrorman. 
""")