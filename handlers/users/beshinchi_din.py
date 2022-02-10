from aiogram import types
from keyboards.default.diniy_kalima import din
from loader import dp


# Echo bot
@dp.message_handler(text="☝️OLTI DINIY KALIMA☝️")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/salom9899/232", caption="Islom dinidagi olti diniy kalima", reply_markup=din),

@dp.message_handler(text="5-Diniy kalima")
async def bot_echo(message: types.Message):
    await message.answer(text="""5. Kalimai istig‘for

Astag‘firulloh, astag‘firulloh, astag‘firulloha ta’ala min kulli zambin aznabtuhu ‘amdan av xotoan sirron va ‘alaniyah. Va atubu ilayhi minaz zambillazi a’lamu va minaz-zambillazi la a’lam. Innaka anta ‘allamul g‘uyub.

Gunohlarni kechishini so‘rash so‘zi: Allohdan gunohlarimni kechishini so‘rayman. Allohdan gunohlarimni kechishini so‘rayman. Alloh taolodan ataylab yo adashib, yashirin yo oshkora qilgan hamma gunohlarimni kechishini so‘rayman. O‘zim bilgan va bilmagan gunohlardan Allohga qaytaman. Albatta, Sen g‘ayblarni bilguchi Zotsan. """)