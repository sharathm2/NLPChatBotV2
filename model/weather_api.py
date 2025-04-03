#Weather API
import requests

def get_weather(city="New York"):
    api_key = "1435e42b1af16b86cbd67556f60cb089"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        res = requests.get(url)
        data = res.json()
        if data["cod"] != 200:
            return f"Sorry, I couldn't find weather for {city}."
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The weather in {city} is {desc}, around {temp}°C."
    except Exception as e:
        return "Sorry, I had trouble getting the weather."
