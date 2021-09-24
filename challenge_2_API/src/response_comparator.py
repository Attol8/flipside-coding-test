import pandas as pd
import requests

class ResponseComparator:
    def __init__(self, url1, url2):
        self.url1 = url1
        self.url2 = url2

        try:
            self.response1 = requests.get(url1)
            self.response1_json = requests.get(url1).json()
            self.response2 = requests.get(url2)
            self.response2_json = requests.get(url2).json()
        except requests.exceptions.RequestException as e:
            print(f'error: {e}')   
       

    def ordered(self, obj):
        if isinstance(obj, dict):
            return sorted((k, self.ordered(v)) for k, v in obj.items())
        if isinstance(obj, list):
            return sorted(self.ordered(x) for x in obj)
        else:
            return obj

    def compare_responses(self):
        return self.ordered(self.response1_json) == self.ordered(self.response2_json)

    def print_output(self):
        is_equal = self.compare_responses()
        if is_equal: print(f'{self.url1} equals {self.url2}')
        else: print(f'{self.url1} not equal {self.url2}')



