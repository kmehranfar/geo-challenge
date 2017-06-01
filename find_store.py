""" Find Store.

Usage:
  find_store --address="<address>"
  find_store --address="<address>" [--units=(mi|km)] [--output=text|json]
  find_store --zip=<zip>
  find_store --zip=<zip> [--units=(mi|km)] [--output=text|json]

Options:
  --zip=<zip>          Find nearest store to this zip code. If there are multiple best-matches, return the first.
  --address=<address>  Find nearest store to this address. If there are multiple best-matches, return the first.
  --units=(mi|km)      Display units in miles or kilometers [default: mi]
  --output=(text|json) Output in human-readable text, or in JSON (e.g. machine-readable) [default: text]

 """
 
import sys
import json
import googlemaps

import pandas as pd
from math import radians, cos, sin, asin, sqrt
df = pd.read_csv('./store-locations.csv')

AVG_EARTH_RADIUS = 6371  # in km

def haversine(row, point2, miles=False):
    """ Calculate the great-circle distance between two points on the Earth surface.
    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.
    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))
    :output: Returns the distance bewteen the two points.
    The default unit is kilometers. Miles can be returned
    if the ``miles`` parameter is set to True.
    """
    # unpack latitude/longitude
    lat1 = row['Latitude']
    lng1 = row['Longitude']
    lat2, lng2 = point2

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
    h = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))
    if miles:
        return h * 0.621371  # in miles
    else:
        return h  # in kilometers

def produce_output(location_dict, output_type):
	if output_type == "text":
		print("Nearest store: ", location_dict["Store Name"])
		print("Distance: ", round(location_dict["Calculated Distance"], 2))
		print("Address: ", location_dict["Address"])
		print("City: ", location_dict["City"])
		print("State: ", location_dict["State"])
		print("Zip: ", location_dict["Zip Code"])
	elif output_type == "json":
		print(json.dumps(location_dict))
		
	
def find_nearest_store(geocode_me, output_type="text", is_miles=True):
	gmaps = googlemaps.Client(key='AIzaSyA6xLNRspdD_dTFqAq23P3ql1nxm9IROk8')

	# geocode the address
	try:
		geocode_result = gmaps.geocode(geocode_me)
	except Exceptions as e:
		print(e)
	
	# retrieve coordinates from returned json
	coord = geocode_result[0]['geometry']['location']
	qry_point = (coord['lat'], coord['lng'])

	# calculate the distance from the query point to all locations and store in df
	df['Calculated Distance'] = df.apply(haversine, point2=qry_point, miles=is_miles,axis=1)
	# sort by distance
	result = df.sort_values(by='Calculated Distance',ascending=True)
	# get the first one
	row = result.head(n=1)
	# extract the fields as a dictionary
	location = row.to_dict(orient='records')
	location_dict = location[0]
	# and output
	produce_output(location_dict, output_type)
	

from docopt import docopt

def main():
	arguments = docopt(__doc__, version='Find Store 1.0')
	geocode_me = ""
	is_miles = True
	output_type = "text"
	if arguments['--address'] is not None:
		geocode_me = arguments['--address']
	if arguments['--zip'] is not None:
		geocode_me = arguments['--zip']
	if arguments['--units'] == 'km':
		is_miles = False
	if arguments['--output'] == 'json':
		output_type = "json"
	find_nearest_store(geocode_me, output_type, is_miles)
	
if __name__ == '__main__':
	main()
	