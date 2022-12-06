import pytest
import requests

# This test is to check basemap is accessible or not
def test_basemap_url():                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    url = "https://services.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer"                                                                                                               
    response = requests.get(url)
    assert response.status_code == 200

# This test is to check geocode service is accessible or not
def test_geocode_server_url():
    url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer"
    response = requests.get(url)
    assert response.status_code == 403

# This test is to check geocode suggests is returing correct results for redlands location
def test_geocode_suggests():
    url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/suggests?f=json&text=redlands&maxSuggestions=6&distance=50000"
    response = requests.get(url)
    print(response)
    assert len(response.json()['suggestions']) == 6


# Tests below are to check YELP API
@pytest.mark.parametrize("categories,location,recordlimit,count", [("active,localservices,health","91711",30,30),("food,shopping","91711",20,20)])
def test_yelp_search(yelpclient, categories, location, recordlimit, count):
    results = yelpclient.querydata(categories, location, 20, recordlimit)
    assert len(results['businesses']) == count

@pytest.mark.parametrize("categories,recordlimit,count", [("restaurants,hospitals,urgent_care",30,30),("dentists,electronicsrepair",20,20)])
def test_yelp_search_2(yelpclient, categories, recordlimit, count):
    results = yelpclient.querydata2(categories,20,recordlimit)
    assert len(results['businesses']) == count

# Tests below are to check YELP Categories
def test_Categories(yelpcategoriesdata):
    assert len(yelpcategoriesdata.getcategories()) == 5

@pytest.mark.parametrize("category,count",[("active",9),("food",6),("health",7),("localservices",6),("shopping",8)])
def test_Categories(yelpcategoriesdata, category, count):
    assert len(yelpcategoriesdata.getsubcategories(category)) == count
