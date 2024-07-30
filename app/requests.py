import requests
import time
import asyncio

russian = ['солнечно', 'переменная облачность', 'облачно', 'пасмурно', 'туман', 'возможен кратковременный дождь', 'возможен локальный снег', 'возможен локальный мокрый снег', 'возможен неравномерный ледяной дождь', ' возможны грозовые вспышки', 'метель', 'метель', 'туман', 'леденящий туман', 'небольшой мелкий дождь', 'небольшой дождь', 'ледяная морось', 'сильный ледяной дождь', 'небольшой мелкий дождь', 'слабый дождь', 'иногда умеренный дождь', 'умеренный дождь', 'иногда сильный дождь', 'сильный дождь', 'слабый ледяной дождь', 'умеренный или сильный ледяной дождь', 'слабый мокрый снег', ' умеренный или сильный мокрый снег', 'небольшой снег', 'небольшой снег', 'небольшой умеренный снег', 'умеренный снег', 'плохой сильный снег', 'сильный снегопад', 'ледяная крупа', 'слабый ливень', 'умеренный или сильный ливень', 'проливной ливень', 'легкий ливень с мокрым снегом', 'умеренный или сильный ливень с мокрым снегом', 'слабый ливневый снег', 'умеренный или сильный ливневый снег', 'легкий ливневый дождь из ледяной крупы', 'умеренный или сильный ливень из ледяной крупы', 'плохой мелкий дождь с громом', 'умеренный или сильный дождь с грозой', 'плохой мелкий снег с грозой', 'умеренный или сильный снегопад с грозой', 'неподалёку мелкий дождь'] 
english =  ['sunny', 'partly cloudy', 'cloudy', 'overcast', 'mist', 'patchy rain possible', 'patchy snow possible', 'patchy sleet possible', 'patchy freezing drizzle possible', 'thundery outbreaks possible', 'blowing snow', 'blizzard', 'fog', 'freezing fog', 'patchy light drizzle', 'light drizzle', 'freezing drizzle', 'heavy freezing drizzle', 'patchy light rain', 'light rain', 'moderate rain at times', 'moderate rain', 'heavy rain at times', 'heavy rain', 'light freezing rain', 'moderate or heavy freezing rain', 'light sleet', 'moderate or heavy sleet', 'patchy light snow', 'light snow', 'patchy moderate snow', 'moderate snow', 'patchy heavy snow', 'heavy snow', 'ice pellets', 'light rain shower', 'moderate or heavy rain shower', 'torrential rain shower', 'light sleet showers', 'moderate or heavy sleet showers', 'light snow showers', 'moderate or heavy snow showers', 'light showers of ice pellets', 'moderate or heavy showers of ice pellets', 'patchy light rain with thunder', 'moderate or heavy rain with thunder', 'patchy light snow with thunder', 'moderate or heavy snow with thunder', 'patchy rain nearby']
 
'patchy rain nearby'
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
        answer = ''
        f = 0
        for hour in prediction_weather:
            if int(hour['time'][11:13]) > current_time:
                answer += f'В {hour['time'][11:13]} часов будет {hour['temp_c']}, {russian[(english.index((hour['condition']['text']).lower().rstrip()))]}. \n'
                f += 1
                if f >= 3:
                    break
        return answer

    except:
        return "Неправильно введен город"
