import requests 
import re 
from constants import Car, car_strings, next_page_string, store_string
from urllib.parse import urlparse

makes_to_keep = ['LANDROVER', "LAND ROVER"]
models_to_keep = ['DISCO', 'DISCOVERY', 'DISC']
all_cars = []

def filter_found_cars(found_cars:list): 
    found_cars = list(filter(lambda u :1999 <= int(u.year) <= 2010, found_cars))
    found_cars = list(filter(lambda u: u.make in makes_to_keep, found_cars))
    found_cars = list(filter(lambda u: u.model.upper() in models_to_keep, found_cars))
    return found_cars

def build_cars(location_code): 
    limit_str = "&Limit=100"
    url = "https://www.lkqpickyourpart.com/inventory/{location_code}/?page=1"+limit_str
    base_url ='https://www.lkqpickyourpart.com'
    html = requests.get(url).text
    found_cars = [Car(year=year, make=make, model=model) for year, make, model in  re.findall(car_strings, html)]
    if filter_found_cars(found_cars):
        all_cars.extend(found_cars)
    while next_page_link:=re.findall(next_page_string, html):
        print(next_page_link)   
        html = requests.get(base_url+next_page_link[0]+limit_str).text
        found_cars = [Car(year=year, make=make, model=model) for year, make, model in re.findall(car_strings, html)]
        if filter_found_cars(found_cars):
            print('Found a disco!')
            print(found_cars)
            all_cars.extend(found_cars)
        
if __name__ == "__main__": 
    url = "https://www.lkqpickyourpart.com/parts/riverside-1290/"
    store = re.findall(store_string, url)[0]
    build_cars(store)
