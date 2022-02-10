import requests as requests
from aiogram import types

from data.config import BOT_TOKEN
from keyboards.default.Namoz_oqish import tugmalar
from keyboards.default.menu import tugma
from loader import dp, bot


# Echo bot
@dp.message_handler(text="📖NAMOZ O'QISH📖")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/salom9899/11", caption="📖NAMOZ O'QISH📖 bolimiga xush kelibsiz\nPastdagi menulardan birini tanlang",reply_markup=tugmalar)
@dp.message_handler(text="Azon")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio="https://t.me/salom9899/219",caption="Azon Mishari Rashid qiroati\n\n👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")


@dp.message_handler(text="📖NAMOZ O'QISH📖")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/salom9899/11",caption="📖NAMOZ O'QISH📖 bolimiga xush kelibsiz\nPastdagi menulardan birini tanlang",reply_markup=tugmalar)
@dp.message_handler(text="1.Bomdod namozi")
async def bot_echo(message: types.Message):
    await message.answer_video(video="https://t.me/salom9899/198", caption="Bomdod namozi Erkaklar uchun\n\n👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")
    await message.answer_video(video="https://t.me/salom9899/199",caption="Bomdod namozi Ayollar uchun Xanafiy mazxabida\n\n👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")

@dp.message_handler(text="📖NAMOZ O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖NAMOZ O'QISH📖",reply_markup=tugmalar)

@dp.message_handler(text="2.Peshin namozi")
async def bot_echo(message: types.Message):
    await message.answer_video(video="https://t.me/salom9899/200", caption="Peshin namozi Erkaklar uchun \n\n👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")
    await message.answer_video(video="https://t.me/salom9899/201", caption="Peshin namozi Ayollar uchun Xanafiy mazxabida \n\n👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")

@dp.message_handler(text="📖NAMOZ O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖NAMOZ O'QISH📖",reply_markup=tugmalar)

@dp.message_handler(text="3.Asr namozi")
async def bot_echo(message: types.Message):
    await message.answer_video(video="https://t.me/salom9899/202", caption="Asr namozi Erkaklar uchun \n\n👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")
    await message.answer_video(video="https://t.me/salom9899/203", caption="Asr namozi Ayollar uchun Xanafiy mazxabida \n\n👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")

@dp.message_handler(text="📖NAMOZ O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖NAMOZ O'QISH📖",reply_markup=tugmalar)

@dp.message_handler(text="4.Shom namozi")
async def bot_echo(message: types.Message):
    await message.answer_video(video="https://t.me/salom9899/204", caption="Shom namozi Erkaklar uchun \n\n👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")
    await message.answer_video(video="https://t.me/salom9899/205", caption="Shom namozi Ayollar uchun Xanafiy mazxabida \n\n👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")

@dp.message_handler(text="📖NAMOZ O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖NAMOZ O'QISH📖",reply_markup=tugmalar)

@dp.message_handler(text="5.Xufton namozi")
async def bot_echo(message: types.Message):
    await message.answer_video(video="https://t.me/salom9899/206", caption="Xufton namozi Erkaklar uchun \n\n👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")
    await message.answer_video(video="https://t.me/salom9899/207", caption="Xufton namozi Ayollar uchun Xanafiy mazxabida \n\n👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")

@dp.message_handler(text="👈Orqaga qaytish")
async def bot_echo(message: types.Message):
    await message.answer(text="Ortga muvaffaqiyatli qaytdingiz",reply_markup=tugma)