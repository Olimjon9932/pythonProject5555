from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(text="🤲NAMOZ KITOBI🤲")
async def bot_echo(message: types.Message):
    await message.answer_document(document="https://t.me/salom9899/215")#, caption="👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817"),
    await message.answer_document(document="https://t.me/salom9899/216")#, caption="👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817"),
    await message.answer_document(document="https://t.me/salom9899/217")#, caption="👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817"),
    await message.answer_document(document="https://t.me/salom9899/218")#, caption="👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")
