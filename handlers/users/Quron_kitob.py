from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(text="🕋QURON KITOB🕋")
async def bot_echo(message: types.Message):
    await message.answer_document(document="https://t.me/salom9899/210")#, caption="👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817"),
    await message.answer_document(document="https://t.me/salom9899/211")#, caption="👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817"),
    await message.answer_document(document="https://t.me/salom9899/212")#, caption="👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817"),
    await message.answer_document(document="https://t.me/salom9899/214")#, caption="👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")
