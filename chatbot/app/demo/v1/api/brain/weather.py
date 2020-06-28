# this function retrieve weather data from OneWeatherMap
import requests

api_key = "1107a0fba97c73f3f5d572d3b9f3fa54"


def get_weather(city):
	url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}"
	# get the data from OneWeatherMap
	response = requests.get(url)
	weather_data = response.json()

	# extract weather description and temperature from the weather data
	weather = weather_data['weather'][0]['description']
	temp = str(weather_data['main']['temp'])

	reply = "the weather in " + city + " is " + weather + ", and the temperature is " + temp + " celsius degree"
	reply += '.'
	return reply
