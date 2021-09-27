import unittest
import pandas as pd
import requests
from src.response_comparator import ResponseComparator

class TestComparator(unittest.TestCase):

    def test_compare_equal(self):
        url1 = 'https://reqres.in/api/users/3'
        url2 = 'https://reqres.in/api/users/3'
        response_comparator = ResponseComparator(url1, url2)
        self.assertEqual(response_comparator.compare_responses(), True)

    def test_compare_not_equal(self):
        url1 = 'https://reqres.in/api/users/3'
        url2 = 'https://reqres.in/api/users/2'
        response_comparator = ResponseComparator(url1, url2)
        self.assertEqual(response_comparator.compare_responses(), False)

if __name__ == '__main__':
    unittest.main()