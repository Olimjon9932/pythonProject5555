from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(text="📚SAODAT ASRI QISSALARI  KITOBI📚")
async def bot_echo(message: types.Message):
    await message.answer_document(document="https://t.me/salom9899/223"),#caption="👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")
    await message.answer_document(document="https://t.me/salom9899/222"), #caption="👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817"),
    await message.answer_document(document="https://t.me/salom9899/224"), #caption="👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817"),
    await message.answer_document(document="https://t.me/salom9899/225"), #caption="👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817"),
    await message.answer_document(document="https://t.me/salom9899/221"), #caption="👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817")
