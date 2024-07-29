from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Погода сейчас'), KeyboardButton(text='Погода позже')],
    ]
)