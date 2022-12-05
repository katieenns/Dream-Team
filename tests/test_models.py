import pytest
import requests
from website.models.yelp import YELPSearch
from website.models.categories import YELPCategories
from website import create_app

YELP_API_KEY="fIVaHCe-6zTYy-QPCngxNscKSIIqIhUKs-U9t09yppe7sFq6QqPwex9wYstdlPbxnTHeD6mdR7Y2L-RFAtL4WqClktJsWgOi7vZi_9cToCAUA_OQraBNuU5W-UAsX3Yx"
YELP_URL="https://api.yelp.com/v3/businesses/search"
                                                                                                              
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
@pytest.fixture
def yelpclient():
    return YELPSearch(YELP_API_KEY, YELP_URL)

@pytest.mark.parametrize("categories,location,recordlimit,count", [("active,localservices,health","91711",30,30),("food,shopping","91711",20,20)])
def test_yelp_search(yelpclient, categories, location, recordlimit, count):
    results = yelpclient.querydata(categories, location, 20, recordlimit)
    assert len(results['businesses']) == count

@pytest.mark.parametrize("categories,recordlimit,count", [("restaurants,hospitals,urgent_care",30,30),("dentists,electronicsrepair",20,20)])
def test_yelp_search_2(yelpclient, categories, recordlimit, count):
    results = yelpclient.querydata2(categories,20,recordlimit)
    assert len(results['businesses']) == count

# Tests below are to check YELP Categories
@pytest.fixture
def yelpcategoriesdata():
    return YELPCategories()   

def test_Categories(yelpcategoriesdata):
    assert len(yelpcategoriesdata.getcategories()) == 5

@pytest.mark.parametrize("category,count",[("active",9),("food",6),("health",7),("localservices",6),("shopping",8)])
def test_Categories(yelpcategoriesdata, category, count):
    assert len(yelpcategoriesdata.getsubcategories(category)) == count


@pytest.fixture
def app():
    app = create_app()
    return app

# Test workflow
@pytest.mark.parametrize('url', [('/'), ('/login'), ('/subcategory/active'), ('/subcategory/food'), ('/static/images/pin-30.png'),('/yelpsearch/10$30$$$hospitals'),
                            ('/static/index.js')])
def test_200(app, url):
    with app.test_client() as test_client:
        test = test_client.get(url)
    assert test.status_code == 200

@pytest.mark.parametrize('url', [('/logout'),('/admin'), ('/add_category'), ('/delete_category'), ('/update_category'), ('/subcategories')])
def test_500(app, url):
    with app.test_client() as test_client:
        test = test_client.get(url)
    assert test.status_code == 500

@pytest.mark.parametrize('url', [('/sign-up')])
def test_404(app, url):
    with app.test_client() as test_client:
        test = test_client.get(url)
    assert test.status_code == 404