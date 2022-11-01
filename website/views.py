from flask import Blueprint, render_template, request, jsonify, current_app
from website.models.yelp import YELPSearch
from website.models.categories import YELPCategories

views = Blueprint('views', __name__)

yelpdetails = '{}'

@views.route('/', methods=['GET', 'POST'])
def home():
    yelpdetails = '{}'
    categorylist = YELPCategories()
    return render_template("home.html", yelpdata=yelpdetails, yelpcategories=categorylist.getcategories())


@views.route('/yelpsearch', methods=['GET', 'POST'])
def yelpsearch():
    yelpdetails = '{}'
    if request.method == 'POST':
        categorylist = YELPCategories()
        yelpsubcategories = request.form.getlist('yelpSubCategory')
        print('Category is ' + str(yelpsubcategories))
        yelpradius = request.form.get('yelpRadius')
        print('Radius is ' + str(yelpradius))
        yelprecordlimit = request.form.get('yelpRecordLimit')
        print('Record Limit is ' + str(yelprecordlimit))
        yelplocationlat = request.form.get('yelpLocationLat')
        print('Latitude is ' + str(yelplocationlat))
        yelplocationlong = request.form.get('yelpLocationLong')
        print('Longitude is ' + str(yelplocationlong))
        yelpsearchcls = YELPSearch(current_app.config["YELP_ACCESS_KEY"], current_app.config["YELP_URL"])
        yelpdetails = yelpsearchcls.querydata2(yelpsubcategories, int(yelpradius), int(yelprecordlimit), yelplocationlat, yelplocationlong)['businesses']
    return render_template("home.html", yelpdata=yelpdetails, yelpcategories=categorylist.getcategories())


@views.route("/yelpsearch2/<parameters>")
def yelpsearch2(parameters):
    paramvalues = parameters.split("$")
    yelpsubcategories = paramvalues[4]
    yelpradius = paramvalues[0]
    yelprecordlimit = paramvalues[1]
    yelplocationlat = paramvalues[2]
    yelplocationlong = paramvalues[3]
    yelpsearchcls = YELPSearch(current_app.config["YELP_ACCESS_KEY"], current_app.config["YELP_URL"])
    yelpdetails = yelpsearchcls.querydata2(yelpsubcategories, int(yelpradius), int(yelprecordlimit), yelplocationlat, yelplocationlong)
    return jsonify(yelpdetails)


@views.route("/subcategory/<value>")
def sucategories(value):
    OutputArray = []
    categorylist = YELPCategories()
    subcats = categorylist.getsubcategories(value)
    for key, pair in subcats.items():
        outputObj = {
            'id': key,
            'name': pair}
        OutputArray.append(outputObj)
    return jsonify(OutputArray)
    

