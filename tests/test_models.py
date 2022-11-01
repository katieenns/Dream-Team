import pytest
import requests
from website.models.yelp import YELPSearch
from website.models.categories import YELPCategories

YELP_API_KEY="fIVaHCe-6zTYy-QPCngxNscKSIIqIhUKs-U9t09yppe7sFq6QqPwex9wYstdlPbxnTHeD6mdR7Y2L-RFAtL4WqClktJsWgOi7vZi_9cToCAUA_OQraBNuU5W-UAsX3Yx"
YELP_URL="https://api.yelp.com/v3/businesses/search"
                                                                                                              
# This test is to check basemap is accessible or not
@pytest.mark.basemap
def test_basemap_url():                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    url = "https://services.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer"                                                                                                               
    response = requests.get(url)
    assert response.status_code == 200

# This test is to check geocode service is accessible or not
@pytest.mark.geocoding
def test_geocode_server_url():
    url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer"
    response = requests.get(url)
    assert response.status_code == 403

# This test is to check geocode suggests is returing correct results for redlands location
@pytest.mark.geocoding
def test_geocode_suggests():
    url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/suggests?f=json&text=redlands&maxSuggestions=6&distance=50000"
    response = requests.get(url)
    print(response)
    assert len(response.json()['suggestions']) == 6

# Tests below are to check YELP API
@pytest.fixture
def yelpclient():
    return YELPSearch(YELP_API_KEY, YELP_URL)

@pytest.mark.YELP
@pytest.mark.parametrize("categories,location,recordlimit,count", [("active,localservices,health","91711",30,30),("food,shopping","91711",20,20)])
def test_yelp_search(yelpclient, categories, location, recordlimit, count):
    results = yelpclient.querydata(categories, location, 20, recordlimit)
    assert len(results['businesses']) == count

@pytest.mark.YELP
@pytest.mark.parametrize("categories,recordlimit,count", [("restaurants,hospitals,urgent_care",30,30),("dentists,electronicsrepair",20,20)])
def test_yelp_search_2(yelpclient, categories, recordlimit, count):
    results = yelpclient.querydata2(categories,20,recordlimit)
    assert len(results['businesses']) == count

# Tests below are to check YELP Categories
@pytest.fixture
def yelpcategoriesdata():
    return YELPCategories()   

@pytest.mark.YELPCategories
def test_Categories(yelpcategoriesdata):
    assert len(yelpcategoriesdata.getcategories()) == 5

@pytest.mark.YELPCategories
@pytest.mark.parametrize("category,count",[("active",9),("food",6),("health",7),("localservices",6),("shopping",8)])
def test_Categories(yelpcategoriesdata, category, count):
    assert len(yelpcategoriesdata.getsubcategories(category)) == count