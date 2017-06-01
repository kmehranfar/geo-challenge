from find_store import find_nearest_store

def test_fs_10001(capsys):
	find_nearest_store("10001")
	out, err = capsys.readouterr()
	assert out =="""Nearest store:  Jersey City
Distance:  2.42
Address:  100 14th St
City:  Jersey City
State:  NJ
Zip:  07310-1202
""" 

def test_fs_10001_km(capsys):
	find_nearest_store("10001",is_miles=False)
	out, err = capsys.readouterr()
	assert out =="""Nearest store:  Jersey City
Distance:  3.89
Address:  100 14th St
City:  Jersey City
State:  NJ
Zip:  07310-1202
""" 

def test_fs_10001_json(capsys):
	find_nearest_store("10001",output_type="json")
	out, err = capsys.readouterr()
	assert out =="""{"Store Name": "Jersey City", "Store Location": "NWC Washington Blvd & 14th St", "Address": "100 14th St", "City": "Jersey City", "State": "NJ", "Zip Code": "07310-1202", "Latitude": 40.73260379999999, "Longitude": -74.036007, "County": "Hudson County", "Calculated Distance": 2.4169121709631023}
"""

def test_fs_address(capsys):
	find_nearest_store("4729 via altamira, thousand oaks, ca")
	out, err = capsys.readouterr()
	assert out == """Nearest store:  Thousand Oaks
Distance:  2.61
Address:  2705 Teller Rd
City:  Thousand Oaks
State:  CA
Zip:  91320-1190
"""

def test_fs_address_km(capsys):
	find_nearest_store("4729 via altamira, thousand oaks, ca", is_miles=False)
	out, err = capsys.readouterr()
	assert out == """Nearest store:  Thousand Oaks
Distance:  4.2
Address:  2705 Teller Rd
City:  Thousand Oaks
State:  CA
Zip:  91320-1190
"""
	
def test_fs_address_json(capsys):
	find_nearest_store("4729 via altamira, thousand oaks, ca", output_type="json")
	out, err = capsys.readouterr()
	assert out == """{"Store Name": "Thousand Oaks", "Store Location": "NWC Camino dos Rios & Marion", "Address": "2705 Teller Rd", "City": "Thousand Oaks", "State": "CA", "Zip Code": "91320-1190", "Latitude": 34.1908559, "Longitude": -118.933996, "County": "Ventura County", "Calculated Distance": 2.609884444221991}
"""