import flask
import requests

def get_info(categories):
    MY_API_KEY = "Gx6cNUQtLg8xrSG2EUkvKVA_d_wRe63rtQjmMbQf7iOE" \
                 "7J4rsSLGW9iZeuOz7joNy_pPTt8mTvHhXg_Xn6ZB4KCocIm-0SuPf" \
                 "voEIko4eLbKQl4hVnYTF9ANvPktY3Yx"
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': f"Bearer {MY_API_KEY}"}
    # List to hold what is returned from requests call
    responses = []
    # Call requests to get API return for businesses in spec category
    for i, category in enumerate(categories):
        params = {'location': '91711', 'limit': 1, 'categories': category}
        resp = requests.get(url, headers=headers, params=params)
        # resp.json() returns resp.content as a dict rather than what resp.content returns (byte)
        responses.append(resp.json())
    return responses

def create_lists(cat_list, business_dict, category):
    try:
        cat_list.append((business_dict['name'], business_dict[category]))
    except KeyError:
        cat_list.append((business_dict['name'], 'none'))

def get_lists(response):
    # Same keys for each dict in the responses list
    outside_keylist = ["businesses", "total", "region"]
    # same keys for all bus dicts as well
    inside_keylist = ['id', 'alias', 'name', 'image_url', 'is_closed', 'url', 'review_count', 'categories',
                      'rating', 'coordinates', 'transactions', 'price', 'location', 'phone', 'display_phone',
                      'distance']
    # Create lists with info for each place
    ratings = []
    price = []
    pickup_delivery = []
    is_closed = []
    latlong = []

    # Gather restaurant info
    for dicts in response:
        # bus variable is a dict with all of the information about a business
        for bus in dicts[outside_keylist[0]]:
            # ex. get ratings for each place, filter or sort high to low
            create_lists(ratings, bus, 'rating')
            create_lists(price, bus, 'price')
            create_lists(pickup_delivery, bus, 'transactions')
            create_lists(is_closed, bus, 'is_closed')
            create_lists(latlong, bus, 'coordinates')

    # combine lists ?

    # lat = latlong[x][1]['latitude']
    # long = latlong[x][1]['longitude']

    return ratings, price, pickup_delivery, is_closed, latlong


def main():
    #location = '91711'
    categories = ["food", "active", "arts", "beautysvc", "health"]
    # radius = [5, 10, 15, 20]

    # No return for "bicycles" category
    # Include localservices?? nightlife?? restaurants??
    # Some overlap, esp between beauty and health

    # Should show listed categories with below names, not abbrevs
        # Active Life = active
        # Food = food
        # Arts & Entertainment = arts
        # Beauty & Spas = beautysvc
        # Health & Medical = health
        # Bicycles = bicycles

    # something like for cat in categories, user will choose, send that chosen list to get_info to return

    # url and headers will remain the same, categories are the ones chosen by user, location = spec on map
    # include limit # as something user specified?
    response_info = get_info(categories=categories)
    ratings, price, pickup_delivery, is_closed, latlong = get_lists(response_info)


main()