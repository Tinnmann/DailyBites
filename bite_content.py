from urllib import request
import json
import datetime
import requests
from bs4 import BeautifulSoup
import pprint

def get_news():
    dicti = []
    source = 'https://www.foxnews.com/category/media/fox-news-flash'
    res = requests.get(source)
    soup = BeautifulSoup(res.text, 'html.parser')
    info = soup.select(".info-header")
    sep = 'ago '
    for item in info[0:10]:
        txt = item.getText()
        title = txt.split(sep)[1]

        links = item.find_all('a', href=True)
        actual_link = 'https://www.foxnews.com' + links[1].get('href')

        dicti.append({'title': title, 'link':actual_link })

    return(dicti)
   

def get_forecast(coords={'lat': -33.9258, 'lon': 18.4232}):
    try: # collect the weather forecast for the location
        api_key = '*****************' # I've hidden my OpenWeatherMap API key, add one for this to work
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}&units=metric'
        data = json.load(request.urlopen(url))

        forecast = {'city': data['city']['name'], #city name
                    'country': data['city']['country'], #country name
                    'periods': list() #list of forecast data for future periods
                    } 

        for period in data['list'][0:9]: # populate list with next 9 forecast periods 
            forecast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                        'temp': round(period['main']['temp']),
                                        'description': period['weather'][0]['description'].title(),
                                        'icon': f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}.png'})
        
        return forecast

    except Exception as e:
        print(e)


def get_recipe():
    url = "https://tasty.p.rapidapi.com/recipes/list"
    querystring = {"from":"0","size":"20","tags":"under_30_minutes"}
    headers = {
    'x-rapidapi-host': "tasty.p.rapidapi.com",
    'x-rapidapi-key': "****************" # used my own api key here as well
    }

    
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    
    recipes=[]

    for item in data['results']:
        if(item['original_video_url']):
            recipes.append({'name': item['name'],
                'servings': item['num_servings'],
                'url': item['original_video_url']
            })
    
    return recipes     
    


if __name__ == '__main__':
    
    #test the get news function to get the news from Fox
    print("Testing news retrieval...")
    get_news()

    #test weather forecast function 
    print('\nTesting weather forecast...')

    forecast = get_forecast() # get forecast for default location
    if forecast:
        print(f'\nWeather forecast for {forecast["city"]}, {forecast["country"]} is...')
        for period in forecast['periods']:
            print(f' - {period["timestamp"]} | {period["temp"]}°C | {period["description"]}')

    harare = {'lat': -17.8294,'lon': 31.0539} #testing for Harare coordinates
    forecast = get_forecast(coords = harare) #get forecast for Harare ZW

    if forecast:
        print(f'\nWeather forecast for {forecast["city"]}, {forecast["country"]} is...')
        for period in forecast['periods']:
            print(f' - {period["timestamp"]} | {period["temp"]}°C | {period["description"]}')

    invalid = {'lat': 1212.1212 ,'lon': 1212.1212} # invalid coordinates
    forecast = get_forecast(coords = invalid) # get forecast from invalid coordinates

    if forecast is None:
        print('Weather forecast for invalid coordinates returned None')

    get_recipe()