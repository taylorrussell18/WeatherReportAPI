import requests
import time

api_key = "fa89fa482a70d8a4f8aee5effe971eba"
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?units=imperial&"

# Give city name
city_name = input("Search weather in a city: ")

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

class City:

    def __init__(self, name, lat, lon, units="imperial"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(complete_url)
            #response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid={api_key}")
        except:
            print("No Internet Access :(")
        response_json = response.json()
        self.temp = response_json["main"]["temp"]
        self.temp_min = response_json["main"]["temp_min"]
        self.temp_max = response_json["main"]["temp_max"]
        self.timezone = response_json["timezone"]
    def temp_print(self):
        time.sleep(0.5)
        print(f"{city_name} is currently {self.temp}° degrees")
        time.sleep(0.5)
        print(f"Today's High: {self.temp_max}°")
        time.sleep(0.5)
        print(f"Today's Low: {self.temp_min}°")
       
        
my_city = City("Stillwater, Oklahoma", 36.1156, 97.0584)
my_city.temp_print()
