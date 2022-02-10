from aiogram import types
from keyboards.default.diniy_kalima import din
from loader import dp


# Echo bot
@dp.message_handler(text="☝️OLTI DINIY KALIMA☝️")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/salom9899/232", caption="Islom dinidagi olti diniy kalima", reply_markup=din),

@dp.message_handler(text="6-Diniy kalima")
async def bot_echo(message: types.Message):
    await message.answer(text="""6. Kalimai tamjid

Subhanalloh val hamdu lillah va la ilaha illallohu vallohu akbar. La havla va la quvvata illa billahil ‘aliyyil ‘azim. Ma shaallohu kana va ma lam yashalam yakun.

Ulug‘lash so‘zi: Allohning aybu nuqsoni yo‘qdir. Va maqtov Allohgadir. Allohdan o‘zga sig‘iniladigan (iloh) yo‘qdir! Alloh ulug‘dir. Mutloq kuch va quvvat qudratli va buyuk Allohdan o‘zgada yo‘qdir. Alloh nimaniki xohlasa, bo‘ladi, nimaniki xohlamasa, bo‘lmaydi.""")