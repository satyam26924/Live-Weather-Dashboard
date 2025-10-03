!pip install requests

API_KEY = "575a83c5bd9fcbb14c881b7d934eb254"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


import requests
from datetime import datetime, timezone

API_KEY = "575a83c5bd9fcbb14c881b7d934eb254"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    city = city.strip()
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description'].title()
        wind_speed = data['wind']['speed']
        time = datetime.fromtimestamp(data['dt'], tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

        print(f"City: {city_name}, {country}")
        print(f"Last Updated: {time}")
        print(f"Temperature: {temp} °C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Condition: {weather_desc}")
    
    else:
        print("City not found. Please check the spelling or try another city.")


get_weather("Bhaktapur")
