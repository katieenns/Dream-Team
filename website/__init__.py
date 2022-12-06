from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os

db = SQLAlchemy()
DB_NAME = "database.db"

# DB_NAME = "Database/database.db"
# print(os.path.abspath(DB_NAME))

def create_app():
    app = Flask(__name__, template_folder='views')
    app.config['SECRET_KEY'] = 'skdjskdjskdjskdjskdjs'
    app.config['YELP_ACCESS_KEY'] = 'fIVaHCe-6zTYy-QPCngxNscKSIIqIhUKs-U9t09yppe7sFq6QqPwex9wYstdlPbxnTHeD6mdR7Y2L-RFAtL4WqClktJsWgOi7vZi_9cToCAUA_OQraBNuU5W-UAsX3Yx'
    app.config['YELP_URL'] = 'https://api.yelp.com/v3/businesses/search'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.abspath(DB_NAME)}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    from .viewmodels.yelps import yelps
    from .viewmodels.admin import admin

    app.register_blueprint(yelps, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')
    
    from .models.dbmodels import User
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')