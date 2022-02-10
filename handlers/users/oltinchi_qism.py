from aiogram import types
from keyboards.default.oltinchi_qism import olti
from loader import dp, bot


# Echo bot
@dp.message_handler(text="🎧QURON TINGLASH🎧")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/Quron_Mishary_Roshid/4",caption="🎙Barcha suralar Mishari Rashid🎙 \n🎙tomonidan ijro qilingan🎙\n👇Marhamat suralarni tinglang👇",reply_markup=olti)


@dp.message_handler(text="101.Al-Qoria")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/156')

@dp.message_handler(text="102.Al-Takathur")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/157')

@dp.message_handler(text="103.Al-Asr")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/158')

@dp.message_handler(text="104.Al-Hamza")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/159')

@dp.message_handler(text="105.Al-Fil")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/160')

@dp.message_handler(text="106.Al-Quraysh")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/161')

@dp.message_handler(text="107.Al-Maun")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/162')

@dp.message_handler(text="108.Al-Kavsar")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/163')

@dp.message_handler(text="109.Al-Kafirun")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/164')

@dp.message_handler(text="110.Al-Nasr")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/165')

@dp.message_handler(text="111.Al-Masad")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/166')

@dp.message_handler(text="112.Al-Ixlos")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/167')

@dp.message_handler(text="113.Al-Falaq")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/168')

@dp.message_handler(text="114.An-Nas")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/169')

@dp.message_handler(text="6-Qism➡")
async def bot_echo(message: types.Message):
    await message.answer(text="Oltinchi qismga muvaffaqiyatli o'tdingiz", reply_markup=olti)

@dp.message_handler(text="🥰🤲ALLOH ROZI BO'LSIN🤲🥰")
async def bot_echo(message: types.Message):
    await message.answer(text="🧑‍💻🤲ILOHIM AYTGANINGIZ KELSIN🤲🧑‍💻")