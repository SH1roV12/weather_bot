from aiogram.fsm.state import State, StatesGroup

class Get_weater(StatesGroup):
    cur_weather = State()
    pred_weather = State()