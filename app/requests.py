import requests
import time
from app.data import russian, english

async def get_prediction_weather_from_json(current_time, weather):
     answer = ''
     for hour in weather:
            if int(hour['time'][11:13]) > current_time:
                answer += f'В {hour['time'][11:13]} часов будет {hour['temp_c']}, {russian[(english.index((hour['condition']['text']).lower().rstrip()))]}. \n'
                f += 1
                if f >= 3:
                    break

async def get_current_weather(API, city):
    # try:
        req = requests.get(f'https://api.weatherapi.com/v1/current.json?key={API}&q={city}').json()
        current_weather = f'Сейчас за окном {int(req['current']['temp_c'])}, {russian[(english.index((req['current']['condition']['text']).lower().rstrip()))]}'
        return current_weather
    # except:
    #     return "Неправильно введен город"
    
async def get_prediction_weather(API, city):
    try:
        req = requests.get(f'https://api.weatherapi.com/v1/forecast.json?key={API}&q={city}').json()
        current_time = int(time.ctime()[11:13])
        prediction_weather = req['forecast']['forecastday'][0]['hour']
        f = 0
        return await get_prediction_weather_from_json(current_time, prediction_weather)

    except:
        return "Неправильно введен город"
