from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(text="💫RO'ZA DUOSI💫")
async def bot_echo(message: types.Message):
    await message.answer_photo(photo="https://www.savol-javob.com/wp-content/uploads/2020/05/5afc53b68687c.jpg",caption="""Ro'zada og'iz yopish va ochish duolari:     
\nRo'za tutish - Og'iz yopish duosi:
Navaytu an asuma sovma shahri romazona minal fajri ilal mag‘ribi, xolisan lillahi ta’ala. Allohu akbar.
\nManosi: Ramazon oyining rozasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun.Alloh Buyukdir.

Iftorlik - Og'iz ochish duosi:
Allohumma laka sumtu va bika amantu va 'alayka tavakkaltu va 'ala rizqika aftartu, fag'firli ya g'offaru ma qoddamtu va ma axxortu.
\nMa'nosi: Ey, Alloh ushbu ro'zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqingbilan iftor qildim. 
Ey gunohlarni afv qiluvchi Zot, mening avvalgi va keyingi gunohlarimni mag'firat qilgil.
\n\n👨‍🎓Sizga ham shunday bot kerak bo'lsa👉@Tojaliyev_1817""")
