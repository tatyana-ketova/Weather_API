# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import socket
import requests


def weather(city):
    api_key = "****"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = round(data['main']['temp']- 273.15, 2)
        desc = data['weather'][0]['description']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        windspeed = data['wind']['speed']
        print(f'Temperature: {temp} °C')
        print(f'Description: {desc}')
        print(f'Pressure: {pressure}')
        print(f'Humidity: {humidity}')
        print(f'Wind_speed: {windspeed}')

    else:
        print('Error fetching weather data')

if __name__ == "__main__":
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
    response = requests.get("https://ipinfo.io/json")
    data = response.json()
    city = data.get('city')
    print(f'City: {city}')
    weather(city)
