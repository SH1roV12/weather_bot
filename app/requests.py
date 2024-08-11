import time

import aiohttp

from app.data import weather_translate



async def get_prediction_weather_from_json(current_time, weather) -> str:
     answer = ""
     f = 0
     for hour in weather:
            if int(hour['time'][11:13]) > current_time:
                pred_state = weather_translate[((hour['condition']['text']).lower().rstrip())]
                answer += (f'В {hour['time'][11:13]} часов будет {hour['temp_c']}, {pred_state}. \n')
                f += 1
                if f >= 3:
                    break
     return answer

async def get_current_weather(API, city) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.weatherapi.com/v1/current.json?key={API}&q={city}') as response:
            response = await response.json()
            cur_state = weather_translate[((response['current']['condition']['text']).lower().rstrip())]
            current_weather = (f'Сейчас за окном {int(response['current']['temp_c'])}, {cur_state}')
            return current_weather


async def get_prediction_weather(API, city) -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.weatherapi.com/v1/forecast.json?key={API}&q={city}') as response:
                response = await response.json()
                current_time = int(time.ctime()[11:13])
                prediction_weather = response['forecast']['forecastday'][0]['hour']
                return await get_prediction_weather_from_json(current_time, prediction_weather)
    except:
        return "Неправильно введен город"
