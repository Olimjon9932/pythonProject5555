from aiogram import types

from keyboards.inline.inline_buttons import tttt
from keyboards.default.menu import tugma
from loader import dp


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer_photo(photo="https://t.me/salom9899/13",caption="""➖➖➖➖➖➖➖➖➖➖ 
"Assalomu alaykum va Rohmatullohi va Barokatuh😊         
➖➖➖➖➖➖➖➖➖➖         
Do'stlar ushbu Quron Oyatlari barchamizni dilimizni ochadi🌸        
➖➖➖➖➖➖➖➖➖➖         
Barchamizning imonimizni mustahkam va qalblarimizni pok qilsin🤲         
➖➖➖➖➖➖➖➖➖➖➖         
Marhamat menudan kerakli bo'limni tanlang👇""",reply_markup=tugma)

    await message.answer(text="Pastdagi KANAL tugmasini bosib kanalimizga azo bolishni unutmang👇", reply_markup=tttt)