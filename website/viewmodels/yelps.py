from flask import Blueprint, render_template, jsonify, current_app
from website.models.yelp import YELPSearch
from website.models.dbinteraction import DBInteraction

yelps = Blueprint('yelps', __name__)

@yelps.route('/', methods=['GET', 'POST'])
def home():
    query = 'SELECT id, category, description FROM categories'
    dbinteraction = DBInteraction() 
    categories = dbinteraction.ExecuteQuery(query)
    categories_dict = []
    for category in categories:
        categorie_dict = {category.category : category.description}
        categories_dict.append(categorie_dict)
    return render_template("home.html", yelpcategories=categories_dict)

@yelps.route("/yelpsearch/<parameters>")
def yelpsearch2(parameters):
    dbinteraction = DBInteraction()
    paramvalues = parameters.split("$")
    yelpsubcategories = paramvalues[4]
    yelpradius = paramvalues[0]
    yelprecordlimit = paramvalues[1]
    yelplocationlat = paramvalues[2]
    yelplocationlong = paramvalues[3]
    yelpsearchcls = YELPSearch(current_app.config["YELP_ACCESS_KEY"], current_app.config["YELP_URL"])
    yelpdetails = yelpsearchcls.querydata2(yelpsubcategories, int(yelpradius), int(yelprecordlimit), yelplocationlat, yelplocationlong)
    if yelpdetails:
        dbinteraction.AddSearchInformation(yelpsubcategories)
    return jsonify(yelpdetails)


@yelps.route("/subcategory/<value>")
def subcategories(value):
    dbinteraction = DBInteraction() 
    OutputArray = []
    query = 'SELECT subcategory, subdescription FROM subcategories as s JOIN  categories as c ON c.id = s.catid where category='
    query = query + "'" + value + "'"
    subcategories = dbinteraction.ExecuteQuery(query)
    for subcat in subcategories:
        outputObj = {
            'id': subcat.subcategory,
            'name': subcat.subdescription}
        OutputArray.append(outputObj)
    return jsonify(OutputArray)
