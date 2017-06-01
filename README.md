## Motivation

find_store is a script that uses store-locations.csv to find the nearest store to a given address/zip code. I 
considered 3 ways to go about implementing this:

1) Load the data into MySQL (or equivalent) and use a SQL statement to calculate the distance.
2) Load the data using Python's csv module and do all the work in the script.
3) Use pandas.

I chose 3, because it provides more control than 1 and is more flexible than 2. The functionality provided by
this script is only a small subset of questions than can be asked about the data in the location file and pandas
provides the flexibility to answer questions that may come up in the future.

Haversine formula is used for calculating the distance between coordinates.

For text output, I round the decimals to 2 digits. For json output, I do no rounding and provide more fields.

## Installation

I developed this on Windows. I didn't want to do the "#! /usr/bin/env python" without properly testing it. So the script can be run like this:
	`python find_store.py` 
I followed the parameters as outlined in the challenge and running the script without parameters
shows the usage. I am not sure my API key for googlemaps.Client would work. You may have to get your own.

## API Reference

https://github.com/googlemaps/google-maps-services-python
https://github.com/mapado/haversine/blob/master/haversine/__init__.py

## Tests

I used pytest for testing. Tests can be run like this:
	`pytest pytest_find_store.py`