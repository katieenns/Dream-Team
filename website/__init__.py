from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['YELP_ACCESS_KEY'] = 'fIVaHCe-6zTYy-QPCngxNscKSIIqIhUKs-U9t09yppe7sFq6QqPwex9wYstdlPbxnTHeD6mdR7Y2L-RFAtL4WqClktJsWgOi7vZi_9cToCAUA_OQraBNuU5W-UAsX3Yx'
    app.config['YELP_URL'] = 'https://api.yelp.com/v3/businesses/search'
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app