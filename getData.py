import json
import requests

class GetData:
    def get(self, end_point):
        with open('data.json') as json_file:
            data = json.load(json_file)
            needed_data = requests.get(data['base_url']+end_point)
            return needed_data