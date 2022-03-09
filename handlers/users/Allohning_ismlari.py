from aiogram import types
from keyboards.default.Alloh_ismlari import Alloh_ismi
from loader import dp


# Echo bot
@dp.message_handler(text="🕋ALLOHNING GO'ZAL ISMLARI🤲")
async def bot_echo(message: types.Message):
    await message.answer(text=""""Allohning goʻzal ismlari (arabcha: أسماء الله الحسنى, ʾasmāʾ allāh al-Ḥusnā) va ularning mazmuni berilgan. Qurʼoni Karimning Aʼrof surasi 180-oyatida Alloh ismlari haqida shunday deyiladi:
“Allohning goʻzal ismlari bordir. Bas, uni oʻsha ismlar bilan chorlangiz (yod etingiz),Uning ismlarida haqdan ogʻib (nooʻrin joylarda ularni qoʻllaydigan mushrik) kimsalarni tark qilingiz“”
Bu ismlar 99 ta. Ular musulmon ilohiyotida muhim oʻrin tutadi. Alloh ismlari koʻp duolarda qoʻshib aytiladi. 
Qur’oni Karimning Hashr surasida (22-24 oyatlar) Allohning goʻzal ismlarining qisqa roʻyxati bor: ar Rahmon, ar-Rahim, al-Malik, al-Quddus, as-Salom, al-Moʻmin, al-Muhaymin, al-Aziz, al-Jabbor, al-Mutakabbir, al-Xoliq, al-Bori’, al-Musavvir. 
Boshqa hamma ismlar Qur’oni Karimning turli joylarida uchraydigan Alloh sifatlaridan kelib chiqadi va ular bilan bogʻlangan feʼllardan hosil boʻlgan. 
99 ta ism roʻyxati Abu Hurayra r.a (601-679) rivoyat qilgan hadisda bor. Ana shu hadisga koʻra, Muhammad(s.a.v) 99 raqamini keltirgan va har kim Allohning mazkur ismlarini birma-bir aytib chiqsa, albatta, InshaAlloh jannatdan joy ato qilinadi deganlar.
 Boshqa Hadis toʻplamlarida ham Alloh ismlari roʻyxati keltiriladi""", reply_markup=Alloh_ismi)


@dp.message_handler(text="Video")
async def bot_echo(message: types.Message):
    await message.answer_video(video="https://t.me/salom9899/238", caption="Allohning 99 go'zal ismi")

@dp.message_handler(text="Audio")
async def bot_echo(message: types.Message):
    await message.answer_audio(audio="https://t.me/salom9899/239", caption="Allohning 99 go'zal ismi")

@dp.message_handler(text="👈Orqaga qaytish")
async def bot_echo(message: types.Message):
    await message.answer(text="Ortga muvaffaqiyatli qaytdingiz",reply_markup=Alloh_ismi)
