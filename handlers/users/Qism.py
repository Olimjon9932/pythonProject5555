from aiogram import types
from keyboards.default.Qism import qism
from loader import dp, bot


# Echo bot
@dp.message_handler(text="🎧QURON TINGLASH🎧")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/Quron_Mishary_Roshid/4",caption="🎙Barcha suralar Mishari Rashid🎙 \n🎙tomonidan ijro qilingan🎙\n👇Marhamat suralarni tinglang👇",reply_markup=qism)


@dp.message_handler(text="21.Al-Anbiyo")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/75')

@dp.message_handler(text="22.Al-Haj")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/76')

@dp.message_handler(text="23.Al-Mu'minun")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/77')

@dp.message_handler(text="24.Al-Nur")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/78')

@dp.message_handler(text="25.Al-Furqon")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/79')

@dp.message_handler(text="26.Al-Shuaro")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/80')

@dp.message_handler(text="27.Al-Naml")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/81')

@dp.message_handler(text="28.Al-Qasas")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/82')

@dp.message_handler(text="29.Al-Ankobut")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/83')

@dp.message_handler(text="30.Al-Rum")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/84')

@dp.message_handler(text="31.Al-Luqmon")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/85')

@dp.message_handler(text="32.Al-Sajda")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/86')

@dp.message_handler(text="33.Al-Ahzob")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/87')

@dp.message_handler(text="34.Al-Saba'")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/88')

@dp.message_handler(text="35.Al-Fotir")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/89')

@dp.message_handler(text="36.Al-Yasin")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/90')

@dp.message_handler(text="37.Al-Soffat")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/91')

@dp.message_handler(text="38.Al-Sod")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/92')

@dp.message_handler(text="39.Al-Zumar")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/93')

@dp.message_handler(text="40.Al-G'ofir")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/94')

@dp.message_handler(text="2-Qism➡")
async def bot_echo(message: types.Message):
    await message.answer(text="Ikkinchi qismga muvaffaqiyatli o'tdingiz",reply_markup=qism)