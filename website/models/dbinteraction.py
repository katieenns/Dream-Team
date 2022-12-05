from website import db
from .dbmodels import Categories, Subcategories, User, SearchTransactions
from werkzeug.security import generate_password_hash, check_password_hash

class DBInteraction:
    
    def __init__(self):
        pass
    
    def QueryUser(self, email):
        user = User.query.filter_by(email=email).first()
        return user
    
    def QueryAllUsers(self):
        users = User.query.all()
        return users
    
    def CheckPasswordHash(self, user, password):
        if check_password_hash(user.password, password):
            return True
        else:
            return False
    
    def QueryCategory(self, txtcategory):
        objcategory = Categories.query.filter_by(category=txtcategory).first()
        return objcategory
    
    def QueryCategoryById(self, getid):
        objcategory = Categories.query.filter_by(id=getid).first()
        return objcategory
    
    def QuerySubcategory(self, txtsubcategory):
        objcategory = Subcategories.query.filter_by(subcategory=txtsubcategory).first()
        return objcategory
    
    def QuerySubcategoryByID(self, getid):
        objsubcategory = Subcategories.query.filter_by(id=getid).first()
        return objsubcategory
    
    def QuerySubcategoryByCatID(self, catid):
        objsubcategory = Subcategories.query.filter_by(catid=catid).first()
        return objsubcategory
    
    def ExecuteQuery(self, query):
        data = db.engine.execute(query)
        return data
    
    def AddCategory(self, txtcategory, txtdescription, user_name):
        new_category = Categories(category=txtcategory, description=txtdescription, username=user_name)
        db.session.add(new_category)
        db.session.commit()
        return True
    
    def AddSubcategory(self, txtsubcategory, txtsubdescription, cat_id, user_name):
        new_subcategory = Subcategories(subcategory=txtsubcategory, subdescription=txtsubdescription, catid=cat_id, username=user_name)
        db.session.add(new_subcategory)
        db.session.commit()
        return True
    
    def AddUser(self, txtemail, firstname, lastname, _password):
        new_user = User(email=txtemail, first_name=firstname, last_name=lastname, password=generate_password_hash(_password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
    
    def AddRecord(self, objclss):
        db.session.add(objclss)
        db.session.commit()
        return True
    
    def DeleteCategory(self, catid):
        category = Categories.query.filter_by(id=catid).first()
        db.session.delete(category)
        db.session.commit()
        return True
    
    def DeleteSubcategory(self, getid):
        subcategory = Subcategories.query.filter_by(id=getid).first()
        db.session.delete(subcategory)
        db.session.commit()
        return True
    
    def UpdateCategory(self, catid, txtdescription, username):
        category = Categories.query.filter_by(id=catid).first()
        category.description = txtdescription
        category.username = username
        db.session.commit()
    
    def UpdateSubcategory(self, getid, txtsubdescription, username):
        subcategory = Subcategories.query.filter_by(id=getid).first()
        subcategory.subdescription = txtsubdescription
        subcategory.username = username
        db.session.commit()
        return True
    
    def AddSearchInformation(self, subcategorylist):
        subcategoryarray = subcategorylist.split(',')
        for subcategory in subcategoryarray:
            new_searchrecord = SearchTransactions(category=subcategory)
            db.session.add(new_searchrecord)
            db.session.commit()
        return True