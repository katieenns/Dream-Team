from website import create_app
import yelptesting

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/test', methods=["GET", "POST"])
def testfn():
    if request.method == 'GET':
        info = yelptesting.get_info(url='https://api.yelp.com/v3/businesses/search',
                                    headers={'Authorization': f"Bearer {MY_API_KEY}"},
                                    location=91711,
                                    categories=['food'])
        #categories should be what the user selects on the html
    if request.method == "POST":
        # send info above back to html
        pass
