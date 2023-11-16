import requests

def get_temperature(latitude, longitude, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return temperature
    else:
        return "Error: Unable to fetch data"

# Replace with your actual API key
API_KEY = 1f502844abc60f506ccd1fbf36d46d04

# Replace with the desired coordinates
latitude = 40.7128
longitude = -74.0060

temp = get_temperature(latitude, longitude, API_KEY)
print(f"The temperature is {temp} °C")