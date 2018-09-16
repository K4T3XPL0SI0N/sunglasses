import requests, urllib.parse, json

api_url = 'https://sheri.fun/api/v1/'

class FurryAPI():
    def __init__(self):
        pass

    def get(self, endpoint):

        headers = {'Content-Type' : 'application/json'}

        if endpoint == 'mur' or 'yiff':
            response = requests.get(api_url + urllib.parse.quote_plus(endpoint), headers=headers)

            if response.status_code == 200:
                return response.content.decode('utf-8')
            else:
                return None
        else:
            return None