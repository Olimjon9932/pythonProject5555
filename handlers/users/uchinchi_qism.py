from aiogram import types
from keyboards.default.uchinchi_qism import uch
from loader import dp, bot


# Echo bot
@dp.message_handler(text="🎧QURON TINGLASH🎧")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/Quron_Mishary_Roshid/4",caption="🎙Barcha suralar Mishari Rashid🎙 \n🎙tomonidan ijro qilingan🎙\n👇Marhamat suralarni tinglang👇",reply_markup=uch)


@dp.message_handler(text="41.Al-Fussilat")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/95')

@dp.message_handler(text="42.Al-Shuro")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/96')

@dp.message_handler(text="43.Al-Zuhruf")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/97')

@dp.message_handler(text="44.Al-Duhan")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/98')

@dp.message_handler(text="45.Al-Josiya")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/99')

@dp.message_handler(text="46.Al-Ahqof")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/100')

@dp.message_handler(text="47.Al-Muhammad")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/101')

@dp.message_handler(text="48.Al-Fath")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/102')

@dp.message_handler(text="49.Al-Hujurot")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/103')

@dp.message_handler(text="50.Al-Qof")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/104')

@dp.message_handler(text="51.Al-Zariyat")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/105')

@dp.message_handler(text="52.Al-Tur")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/106')

@dp.message_handler(text="53.Al-Najm")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/107')

@dp.message_handler(text="54.Al-Qamar'")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/108')

@dp.message_handler(text="55.Al-Rahmon")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/109')

@dp.message_handler(text="56.Al-Voqea")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/110')

@dp.message_handler(text="57.Al-Hadid")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/111')

@dp.message_handler(text="58.Al-Mujodala")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/112')

@dp.message_handler(text="59.Al-Hashr")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/113')

@dp.message_handler(text="60.Al-Mumtahana")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/114')

@dp.message_handler(text="3-Qism➡")
async def bot_echo(message: types.Message):
    await message.answer(text="Uchinchi qismga muvaffaqiyatli o'tdingiz",reply_markup=uch)