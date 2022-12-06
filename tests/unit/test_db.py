from website.models.dbinteraction import DBInteraction

def test_subcatcount(app):
    catcount = None
    with app.app_context():
        query = 'SELECT count(*) as count FROM subcategories WHERE catid = 1'
        dbinteraction = DBInteraction() 
        categories = dbinteraction.ExecuteQuery(query)
        for row in categories:
            catcount = row.count
    assert catcount == 4

def test_queryallusers(app):
    usercount = None
    with app.app_context():
        query = 'SELECT count(*) as count FROM user'
        dbinteraction = DBInteraction() 
        users = dbinteraction.ExecuteQuery(query)
        for user in users:
            usercount = user.count
    assert usercount > 0