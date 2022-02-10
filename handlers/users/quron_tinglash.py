from aiogram import types
from keyboards.default.quron_tinglash import absd
from keyboards.default.Qism import qism
from loader import dp, bot


# Echo bot
@dp.message_handler(text="🎧QURON TINGLASH🎧")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/Quron_Mishary_Roshid/4",caption="🎙Barcha suralar Mishari Rashid🎙 \n🎙tomonidan ijro qilingan🎙\n👇Marhamat suralarni tinglang👇\n\n👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817",reply_markup=absd)

@dp.message_handler(text="1.Al-Fotiha")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/3')

@dp.message_handler(text="2.Al-Baqara")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/4')

@dp.message_handler(text="3.Al-Oli imron")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/57')

@dp.message_handler(text="4.Al-Niso")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/58')

@dp.message_handler(text="5.Al-Moida")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/64')

@dp.message_handler(text="6.Al-AN'OM")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/155')

@dp.message_handler(text="7.Al-A'rof")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/60')

@dp.message_handler(text="8.Al-Anfol")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/61')

@dp.message_handler(text="9.Al-Tavba")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/62')

@dp.message_handler(text="10.Al-Yunus")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/63')

@dp.message_handler(text="11.Al-Hud")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/65')

@dp.message_handler(text="12.Al-Yusuf")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/66')

@dp.message_handler(text="13.Al-Ra'd")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/67')

@dp.message_handler(text="14.Al-Ibrohim")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/68')

@dp.message_handler(text="15.Al-Hijr")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/69')

@dp.message_handler(text="16.Al-Nahl")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/70')

@dp.message_handler(text="17.Al-Isro")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/71')

@dp.message_handler(text="18.Al-Kahf")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/72')

@dp.message_handler(text="19.Al-Mariyam")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/73')

@dp.message_handler(text="20.Al-Toha")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/74')
