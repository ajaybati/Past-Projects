'''import pyowm

owm = pyowm.OWM('b9c0dbe20f1542573f8cdb4d812ed9fe')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('Chicago,United States')
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
print(w.get_wind())                  # {'speed': 4.6, 'deg': 330}
print(w.get_humidity())              # 87
print(w.get_temperature('fahrenheit')['temp'])  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

'''
'''from urllib.request import Request, urlopen
import urllib.request
from bs4 import BeautifulSoup
import csv
import requests
import re

if __name__=='__main__':
    req = Request("http://eatingatoz.com/food-list/", headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        page = response.read()
        soup = BeautifulSoup(page, 'html.parser')
        data = soup.find(id="post-30")
        ingredients=data.getText().split()
        print(ingredients)
'''
for x in range(5):
    print(x)

'''import zomatopy


config={
  "user_key":"f8f9a12c12f02df267d507d7cae4fc26"
}
    
zomato = zomatopy.initialize_app(config)

city_ID = zomato.get_city_ID("Santa Cruz")
cuisine_dictionary = get_cuisines(city_ID)
print(cuisine_dictionary)
'''
'''import spoonacular as sp
api = sp.API("b0a9f73478msh8c141f72e76ae1ep181836jsnb218b53415d5")

# Parse an ingredient
response = api.parse_ingredients("3.5 cups King Arthur flour", servings=1)
data = response.json()
print(data[0]['name'])
'''
