from aiogram import types
from keyboards.default.diniy_kalima import din
from loader import dp


# Echo bot
@dp.message_handler(text="☝️OLTI DINIY KALIMA☝️")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/salom9899/232", caption="Islom dinidagi olti diniy kalima", reply_markup=din),

@dp.message_handler(text="4-Diniy kalima")
async def bot_echo(message: types.Message):
    await message.answer(text="""4. Kalimai raddi kufr

Allohumma inni a’uzu bika min an ushrika bika shayan va ana a’lam. Va astag‘firuka lima la a’lam. Innaka anta ‘allamul g‘uyub.

Kufrni qaytarish so‘zi: Allohim, Sendan o‘zim bilganim holda Senga biror narsani sherik qilishimdan asrashingni so‘rayman. Sendan o‘zim bilmaganim holda shirk qilib qo‘ygan bo‘lsam, kechishingni tilayman. Albatta, Sen g‘ayblarni bilguvchi Zotsan. """)