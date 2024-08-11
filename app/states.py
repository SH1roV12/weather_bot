from aiogram.fsm.state import State, StatesGroup

class GetWeater(StatesGroup):
    cur_weather = State()
    pred_weather = State()