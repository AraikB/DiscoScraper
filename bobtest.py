import requests
import json 
from html.parser import HTMLParser
import re 
from common.constants import pyp_zip_store_query
from pyzipcode import ZipCodeDatabase


def get_stores_in_zip_code(zip_code):
    zcdb = ZipCodeDatabase()
    in_radius = [z.zip for z in zcdb.get_zipcodes_around_radius(zip_code, 50)] # ('ZIP', radius in miles)
    radius_utf = [x for x in in_radius] # unicode list to utf list
    stores = requests.get(f'https://www.lkqpickyourpart.com/Location/?ZIP={zip_code}&Range=50')
    stores= [store for zip, store in re.findall(pyp_zip_store_query, stores.text) if zip in radius_utf]

    return stores