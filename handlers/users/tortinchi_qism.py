from aiogram import types
from keyboards.default.tortinchi_qism import tort
from loader import dp, bot


# Echo bot
@dp.message_handler(text="🎧QURON TINGLASH🎧")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/Quron_Mishary_Roshid/4",caption="🎙Barcha suralar Mishari Rashid🎙 \n🎙tomonidan ijro qilingan🎙\n👇Marhamat suralarni tinglang👇",reply_markup=tort)


@dp.message_handler(text="61.Al-Sof")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/115')

@dp.message_handler(text="62.Al-Jum'a")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/116')

@dp.message_handler(text="63.Al-Munofiqun")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/117')

@dp.message_handler(text="64.Al-Tag'obun")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/118')

@dp.message_handler(text="65.Al-Taloq")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/119')

@dp.message_handler(text="66.Al-Tahrim")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/120')

@dp.message_handler(text="67.Al-Mulk")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/121')

@dp.message_handler(text="68.Al-Qalam")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/122')

@dp.message_handler(text="69.Al-Haqqa")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/123')

@dp.message_handler(text="70.Al-Maorij")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/124')

@dp.message_handler(text="71.Al-Nuh")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/125')

@dp.message_handler(text="72.Al-Jin")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/126')

@dp.message_handler(text="73.Al-Muzzammil")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/127')

@dp.message_handler(text="74.Al-Muddassir")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/128')

@dp.message_handler(text="75.Al-Qiyomat")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/129')

@dp.message_handler(text="76.Al-Inson")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/130')

@dp.message_handler(text="77.Al-Mursalot")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/131')

@dp.message_handler(text="78.Al-Naba")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/132')

@dp.message_handler(text="79.Al-Nazi'at")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/133')

@dp.message_handler(text="80.Al-Abasa")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/134')

@dp.message_handler(text="4-Qism➡")
async def bot_echo(message: types.Message):
    await message.answer(text="Tortinchi qismga muvaffaqiyatli o'tdingiz", reply_markup=tort)