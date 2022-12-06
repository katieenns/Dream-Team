import pytest
from website.models.dbinteraction import DBInteraction

# Test workflows

#Test login Page
def test_login_available(adminclient):
     with adminclient:
        response = adminclient.get('/login', content_type='html/text')
        assert response.status_code == 200


# Ensure login behaves correctly with correct credentials
def test_login(adminclient,login_credential):
    with adminclient:
        response = adminclient.post('/login', data=dict(email=login_credential['name'], password=login_credential['password']), follow_redirects=True)
        assert response.status_code == 200

# Ensure logout behaves correctly
def test_logout(adminclient,login_credential):
    with adminclient:
        adminclient.post('/login', data=dict(email=login_credential['name'], password=login_credential['password']), follow_redirects=True)
        response = adminclient.get('/logout', follow_redirects=True)
        assert response.status_code == 200

# Ensure categories page is accessible
def test_admincategories(adminclient,login_credential):
    with adminclient:
        adminclient.post('/login', data=dict(email=login_credential['name'], password=login_credential['password']), follow_redirects=True)
        res = adminclient.post('/subcategories')
        assert res.status_code == 200

# Ensure admin home page is accessible
def test_adminhome(adminclient,login_credential):
    with adminclient:
        adminclient.post('/login', data=dict(email=login_credential['name'], password=login_credential['password']), follow_redirects=True)
        res = adminclient.post('/admin')
        assert res.status_code == 200
        
# Test add category
def test_addcategory(adminclient,login_credential):
    with adminclient:
        adminclient.post('/login', data=dict(email=login_credential['name'], password=login_credential['password']), follow_redirects=True)
        res = adminclient.post('/add_category', data=dict(txtcategory='temp23', txtdescription='temp23d', 
                                                          txtsubcategory='tempsub23',txtsubdescription='tempsub23d'))
        assert res.status_code == 200    

# Test update category
def test_updatecategory(adminclient,login_credential):
    with adminclient:
        adminclient.post('/login', data=dict(email=login_credential['name'], password=login_credential['password']), follow_redirects=True)
        query = "Select id from subcategories where subcategory='tempsub23'"
        dbinteraction = DBInteraction() 
        categories = dbinteraction.ExecuteQuery(query)
        for row in categories:
            subcatid = row.id
        res = adminclient.post('/update_category', data=dict(string=subcatid, txtdescription='temp23upd'
                                                          ,txtsubdescription='tempsub23upd'))
        assert res.status_code == 200 

# Test delete category
def test_deletecategory(adminclient,login_credential):
    with adminclient:
        adminclient.post('/login', data=dict(email=login_credential['name'], password=login_credential['password']), follow_redirects=True)
        query = "Select id from subcategories where subcategory='tempsub23'"
        dbinteraction = DBInteraction() 
        categories = dbinteraction.ExecuteQuery(query)
        for row in categories:
            subcatid = row.id
        res = adminclient.post('/delete_category', data=dict(string=subcatid))
        assert res.status_code == 200 
     

# Test URL's      
@pytest.mark.parametrize('url', [('/'), ('/login'), ('/subcategory/active'), ('/subcategory/food'), ('/static/images/pin-30.png'),('/yelpsearch/10$30$$$hospitals'),
                            ('/static/index.js')])
def test_200(app, url):
    with app.test_client() as test_client:
        test = test_client.get(url)
    assert test.status_code == 200


# False positive test to ensure URL does not exists 
@pytest.mark.parametrize('url', [('/sign-up'),('/subscribe')])
def test_404(app, url):
    with app.test_client() as test_client:
        test = test_client.get(url)
    assert test.status_code == 404