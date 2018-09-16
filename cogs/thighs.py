import requests, urllib.parse, json

api_url = 'http://api.rembotofficial.com/images/'

class ThighObject():
    def __init__(self, json_stuff):
        image = json.loads(json_stuff)
        self.url = image['image']['url']
        self.type = image['image']['type']
        self.tag = image['image']['tag']
        self.status_code = image['error']['status']['code']
        self.status = image['error']['status']['status']
        self.message = image['error']['message']
        
class ThighAPI():
    def __init__(self, api_key):
        self.API_KEY = str(api_key)

    def get(self, tag, type):

        headers = {'Content-Type' : 'application/json', 'Authorization' : self.API_KEY, 'type' : type, 'tag' : tag}

        response = requests.get(api_url + urllib.parse.quote_plus(tag), headers=headers)

        if response.status_code == 200:
            return ThighObject(response.content.decode('utf-8'))
        else:
            return None