import json
import requests

api_url = "http://api.openweathermap.org/data/2.5/weather?appid=2ad263b9a82888fd39382d86aa2fc030&mode=json";
api_url += "&lat=43.563795&lon=-65.562125"

weather_results = []

response = requests.get(api_url)

if response.status_code == 200:
    weather_results = json.loads(response.content.decode("utf-8"))

    if weather_results is not None:
        weather_main = weather_results.get("weather")
        weather_main_description = weather_main[0].get("main")

        weather_temp = weather_results["main"]
        weather_temp_description = weather_temp["temp"]

        weather_temp_celsius = weather_temp_description - 273.15

        print(f"{weather_main_description} and {weather_temp_celsius} degrees.")

else:
    print('[!] Request Failed')