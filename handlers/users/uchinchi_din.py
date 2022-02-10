from aiogram import types
from keyboards.default.diniy_kalima import din
from loader import dp


# Echo bot
@dp.message_handler(text="☝️OLTI DINIY KALIMA☝️")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/salom9899/232", caption="Islom dinidagi olti diniy kalima", reply_markup=din),

@dp.message_handler(text="3-Diniy kalima")
async def bot_echo(message: types.Message):
    await message.answer(text="""3. Kalimai tavhid

Ashhadu alla ilaha illallohu vahdahu la sharika lah, lahul mulku va lahul hamd(u) yuhyi va yumit(u) va huva hayyul la yamut(u), biyadihil xoyr(u) va huva ‘ala kulli shayin qodir.

Tanholigiga iqrorlik so‘zi: Tanho Allohdan o‘zga sig‘iniladigan (iloh) yo‘qligiga iqrorman! Allohning sherigi yo‘qdir. Mulk Allohnikidir. Maqtov Allohgadir. (Alloh) tiriltiradi va o‘ldiradi. Ammo O‘zi tirikdir, o‘lmaydi. Yaxshilik Uning ixtiyoridadir va U hamma narsaga qodirdir! """)