import requests 
import re 
from common.constants import Car, pyp_car_string_query, pyp_next_page_query, pyp_store_query,pyp_zip_store_query
from common.helper_functions import filter_found_cars
import requests
import re 
from pyzipcode import ZipCodeDatabase
import time


def build_cars(location_code:str, min_year:int, max_year:int, query_make:str, query_model:str):
    all_cars = [] 
    limit_str = "&Limit=100"
    url = f"https://www.lkqpickyourpart.com/inventory/{location_code}/?page=1"+limit_str
    base_url ='https://www.lkqpickyourpart.com'
    html = requests.get(url).text
    found_cars = [Car(year=year, make=make, model=model) for year, make, model in  re.findall(pyp_car_string_query, html)]
    if found_cars :=filter_found_cars(found_cars, min_year, max_year, query_make, query_model):
        print({f"{car.year} {car.make} {car.model}":url for car in found_cars})
        all_cars.extend({f"{car.year} {car.make} {car.model}":url for car in found_cars})
    while next_page_link:=re.findall(pyp_next_page_query, html):
        
        url = base_url+next_page_link[0]+limit_str   
        html = requests.get(url).text
        found_cars = [Car(year=year, make=make, model=model) for year, make, model in re.findall(pyp_car_string_query, html)]
        if found_cars := filter_found_cars(found_cars, min_year, max_year, query_make, query_model):
            print('Found a disco!')
            print({f"{car.year} {car.make} {car.model}":url for car in found_cars})
            all_cars.extend({f"{car.year} {car.make} {car.model}":url for car in found_cars})
    return all_cars 



def get_stores_in_zip_code(zip_code):
    zcdb = ZipCodeDatabase()
    in_radius = [z.zip for z in zcdb.get_zipcodes_around_radius(zip_code, 50)] # ('ZIP', radius in miles)
    radius_utf = [x for x in in_radius] # unicode list to utf list
    stores = requests.get(f'https://www.lkqpickyourpart.com/Location/?ZIP={zip_code}&Range=50')
    stores= [store for zip, store in re.findall(pyp_zip_store_query, stores.text) if zip in radius_utf]

    return stores

def main(min_year,max_year, query_make, query_model, zip_code):
    pick_your_part = {'PickYourPart':{store:build_cars(store, min_year, max_year, query_make, query_model) for store in get_stores_in_zip_code(zip_code)}}
    return pick_your_part