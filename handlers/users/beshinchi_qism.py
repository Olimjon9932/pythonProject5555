from aiogram import types
from keyboards.default.beshinchi_qism import besh
from loader import dp, bot


# Echo bot
@dp.message_handler(text="🎧QURON TINGLASH🎧")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/Quron_Mishary_Roshid/4",caption="🎙Barcha suralar Mishari Rashid🎙 \n🎙tomonidan ijro qilingan🎙\n👇Marhamat suralarni tinglang👇",reply_markup=besh)


@dp.message_handler(text="81.At-Takvir")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/135')

@dp.message_handler(text="82.Al-Infitar")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/136')

@dp.message_handler(text="83.Al-Mutaffifin")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/137')

@dp.message_handler(text="84.Al-Inshiqaq")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/138')

@dp.message_handler(text="85.Al-Buruj")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/139')

@dp.message_handler(text="86.At-Tariq")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/140')

@dp.message_handler(text="87.Al-Ala")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/141')

@dp.message_handler(text="88.Al-Ghashiyah")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/142')

@dp.message_handler(text="89.Al-Fajr")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/143')

@dp.message_handler(text="90.Al-Balad")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/144')

@dp.message_handler(text="91.Ash-Shams")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/145')

@dp.message_handler(text="92.Al-Lail")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/146')

@dp.message_handler(text="93.Ad-Duha")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/147')

@dp.message_handler(text="94.Ash-Sharh")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/148')

@dp.message_handler(text="95.At-Tin")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/149')

@dp.message_handler(text="96.Al-Alaq")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/150')

@dp.message_handler(text="97.Al-Qadr")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/151')

@dp.message_handler(text="98.Al-Baiyinah")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/152')

@dp.message_handler(text="99.Al-Zalzalah")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/153')

@dp.message_handler(text="100.Al-Adiyat")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio='https://t.me/salom9899/154')

@dp.message_handler(text="5-Qism➡")
async def bot_echo(message: types.Message):
    await message.answer(text="Beshinchi qismga muvaffaqiyatli o'tdingiz", reply_markup=besh)