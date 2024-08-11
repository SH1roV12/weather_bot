import os

from dotenv import load_dotenv
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart 
from aiogram.types import Message

import app.keyboards as kb
from app.requests import get_current_weather, get_prediction_weather
from app.states import GetWeater

load_dotenv()

router = Router()

API = os.getenv('API')



@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('hi', reply_markup=await kb.main_kb())


@router.message(F.text == 'Погода сейчас')
async def ask_city(message: Message, state: FSMContext):
    await state.set_state(GetWeater.cur_weather)
    await message.answer('напиши свой город')


@router.message(F.text == 'Погода позже')
async def ask_city(message: Message, state: FSMContext):
    await state.set_state(GetWeater.pred_weather)
    await message.answer('напиши свой город')


@router.message(GetWeater.cur_weather)
async def wether(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(await get_current_weather(API, message.text))


@router.message(GetWeater.pred_weather)
async def wether(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(await get_prediction_weather(API, message.text))