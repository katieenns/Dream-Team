from flask import Blueprint, render_template, request
#import yelptesting as y


views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # list of cats: ['food', 'arts', etc,] whatver the user has chosen from the drop down
        cats = request.form.getlist('category')
        # Need to add these 2
        radius = request.form.getlist('radius')
        loc = request.form.getlist('zip')
        # returns dictionary of all places
        # resp = y.get_info(cats)
        # # returns all lists
        # ratings, price, pickup_delivery, is_closed, latlong = y.get_lists(resp)
        # print(ratings, price, pickup_delivery, is_closed, latlong)
        print(cats, radius, loc)
    return render_template("home.html")