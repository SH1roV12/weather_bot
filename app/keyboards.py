from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

async def main_kb():
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(KeyboardButton(text='Погода сейчас'), KeyboardButton(text='Погода позже'))
    return keyboard.adjust(2).as_markup()
  