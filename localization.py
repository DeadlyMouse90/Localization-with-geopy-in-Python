#Using the Geopy library to get longitude and latitude from an address

from geopy import Nominatim
import time
from pprint import pprint

app =  Nominatim(user_agent='tutorial')

def get_location_by_address(address):
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return app.get_location_by_address(address)

address = 'Rua Nove de Julho 72, São Paulo - SP'
location = get_location_by_address(address)
pprint(location)
latitude = location['lat']
longitude = location['lon']
print(f'{latitude},{longitude}')
