from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def home():
    from .yelptesting import get_info, get_lists
    if request.method == "POST":
        # list of cats: ['food', 'arts', etc,] whatver the user has chosen from the drop down
        # Want to include more categories (lists inside each larger cat)
        cats = request.form.getlist('category')
    # Need to add radius and loc to base.html
        # 5, 10, 15, 20 miles options -- not sure how to factor that into yelp calls tho
        radius = request.form.getlist('radius')
        # need to do some sort of input validation, or maybe have a drop down list of local zip codes
        loc = request.form.getlist('zip')
        # returns dictionary of all places
        resp = get_info(cats)
        # returns all lists
        ratings, price, pickup_delivery, is_closed, latlong = get_lists(resp)
        # use latlong to plot on map
            # lat = latlong[x][1]['latitude']
            # long = latlong[x][1]['longitude']
        # display ratings, is_closed, price, and pickup/delivery on interface
        print(ratings, price, pickup_delivery, is_closed, latlong)
        #print(cats, radius, loc)
    return render_template("home.html")