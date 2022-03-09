from  aiogram.types import KeyboardButton,ReplyKeyboardMarkup

Alloh_ismi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Video"),
        ],
        [
            KeyboardButton(text="Audio"),
        ],
        [
            KeyboardButton(text="👈Orqaga qaytish")
        ]

    ],
    resize_keyboard=True
)