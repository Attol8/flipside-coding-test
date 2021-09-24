import pandas as pd
import requests

class ResponseComparator:
    def __init__(self, url1, url2):
        url1 = url1
        url2 = url2
        response1 = requests.get(url1)
        response2 = requests.get(url2)

comparator = ResponseComparator('https://reqres.in/api/users/3', 'https://reqres.in/api/users/1')
print(comparator.url1)
