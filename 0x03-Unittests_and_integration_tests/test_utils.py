#!/usr/bin/env python3
import utils
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for testing the function 'access_nested_map'
    which is used to access a nested map with a key list.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test accessing nested map with different paths"""
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, "a", KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(expected):
            utils.access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    @patch('requests.get')
    def test_get_json(self, mock_get):
        # Test cases as a list of tuples
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]

        for url, payload in test_cases:
            with self.subTest(url=url, payload=payload):
                # Set up the mock to return a Mock object with a json method that returns the payload
                mock_get.return_value = Mock()
                mock_get.return_value.json.return_value = payload

                # Call the function
                result = utils.get_json(url)

                # Test that the mocked get method was called exactly once with the url
                mock_get.assert_called_once_with(url)

                # Test that the output of get_json is equal to the payload
                self.assertEqual(result, payload)

                # Reset mock
                mock_get.reset_mock()

if __name__ == "__main__":
    unittest.main()
