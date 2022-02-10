from aiogram import types
from keyboards.default import menu
from loader import dp


# Echo bot
@dp.message_handler(commands="bolim")
async def bot_echo(message: types.Message):
    await message.answer(text="Quroni Karim nomli botimizga xush kelibsiz", reply_markup=menu.tugma)
