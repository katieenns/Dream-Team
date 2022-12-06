import pytest
from website.models.yelp import YELPSearch
from website.models.categories import YELPCategories
from website import create_app
from flask.testing import FlaskClient

YELP_API_KEY="fIVaHCe-6zTYy-QPCngxNscKSIIqIhUKs-U9t09yppe7sFq6QqPwex9wYstdlPbxnTHeD6mdR7Y2L-RFAtL4WqClktJsWgOi7vZi_9cToCAUA_OQraBNuU5W-UAsX3Yx"
YELP_URL="https://api.yelp.com/v3/businesses/search"

@pytest.fixture
def yelpclient():
    return YELPSearch(YELP_API_KEY, YELP_URL)

@pytest.fixture
def yelpcategoriesdata():
    return YELPCategories()  

@pytest.fixture(scope='module')
def app():
    app = create_app()
    return app

@pytest.fixture(scope='module')
def adminclient(app):
    app = app
    ctx = app.test_request_context()
    ctx.push()
    app.test_client_class = FlaskClient
    return app.test_client()

@pytest.fixture
def login_credential():
    return {
        "name": "admin@gmail.com",
        "password": "admin"
    }