import unittest
import pandas as pd
import requests

def mock_response():
    expected = {"data": {"id": 2, "first_name": "Janet", "last_name": "Weaver",
                         "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg"}}
    data = expected['data']
    df = pd.DataFrame(data, index=[0])
    return [expected, data, df]


class TestComparator(unittest.TestCase):

    actual_response = requests.get('https://reqres.in/api/users/2').json()

    def response(self):
        self.assertEqual(self.actual_response, mock_response()[0])

    def test_data_in_response(self):
        self.assertEqual(self.actual_response['data'], mock_response()[1])

    def test_dataframe(self):
        self.assertEqual(pd.DataFrame(self.actual_response['data'], index=[0]), mock_response()[2])


if __name__ == '__main__':
    unittest.main()