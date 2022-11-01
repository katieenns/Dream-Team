from unicodedata import decimal
import requests as requests

class YELPSearch:
    def __init__(self, apikey: str, url: str):
        self.apikey = apikey
        self.url = url
        self.headers = {'Authorization': f"Bearer {apikey}"}
    
    def querydata(self, categories, location, radius, recordlimit):
        radius = radius*1600
        params = {'location': location, 'categories': categories, 'limit': recordlimit, 'radius': radius}
        resp = requests.get(self.url, headers=self.headers, params=params)
        return resp.json()
    
    def querydata2(self, categories, radius: int, recordlimit: int, latitude="", longitude=""):
        radius = radius*1600
        if latitude == "" or longitude == "":
            latitude = 34.104067
            longitude = -117.710737
        params = {'latitude': latitude, 'longitude': longitude, 'categories': categories, 'limit': recordlimit, 'radius': radius}
        resp = requests.get(self.url, headers=self.headers, params=params)
        return resp.json()