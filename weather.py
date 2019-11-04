import requests
import geocoder

class Weather:
    API_KEY = 'e8160db71cd978ea096106fff6512e89'
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
    def __init__(self, location = None):
        self.location = location
        self.is_location = False
        if self.location != None:
            self.is_location = True

    def get_weather_data(self):
        if self.is_location:
            new_url = f'{self.BASE_URL}q={self.location}&appid={self.API_KEY}'
            return self.get_response(new_url)
        else:
            co_ordinates = geocoder.ip('me')
            lat, lon = co_ordinates.latlng
            new_url = f'{self.BASE_URL}lat={lat}&lon={lon}&appid={self.API_KEY}'
            return self.get_response(new_url)

    def get_response(self, the_url):
        try:
            resp_main = requests.get(the_url)
            if resp_main.status_code >= 200 and resp_main.status_code <= 299:
                resp = resp_main.json()
                return (resp['main']['temp'] - 273.15)
        except requests.exceptions.RequestException as e:
            print(e)
            return None

    def present_weather_data(self):
        if self.get_weather_data() != None:
            temperature = self.get_weather_data()
            digree = u"\u2103"
            print(f'{round(temperature)} {digree}')
        else:
            print('Couldn\'t get weather data')

        

            



if __name__ == "__main__":
    print('Please choose one of the following options to get weather data: ')
    print(' 1. Current Location')
    print(' 2. Specific Location')
    option = int(input('Your input: '))

    if option == 1:
        the_weather = Weather()
        the_weather.present_weather_data()
    elif option == 2:
        the_input = str(input('Please enter the location: ')).strip()
        the_weather = Weather(the_input)
        the_weather.present_weather_data()