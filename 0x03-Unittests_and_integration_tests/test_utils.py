#!/usr/bin/env python3
import utils
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from typing import Dict


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
    """
    Defines tests for get_json utility
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, bool]) -> None:
        """
        Test that it returns a valid json payload
        Args:
            test_url (str): url to make a request to
            test_payload (Dict): expected payload from the response
        Returns:
            None
        """
        config = {'return_value.json.return_value': test_payload}
        with patch('requests.get', autospec=True, **config) as mockRequestGet:
            self.assertEqual(utils.get_json(test_url), test_payload)
            mockRequestGet.assert_called_once_with(test_url)
class TestMemoize(unittest.TestCase):
    """
    Defines test for memoize utility function
    """
    def test_memoize(self) -> None:
        """
        Test memoize function
        """
        class TestClass:
            """
            Test class
            """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mockMethod:
            test = TestClass()
            self.assertEqual(test.a_property, mockMethod.return_value)
            self.assertEqual(test.a_property, mockMethod.return_value)
            mockMethod.assert_called_once()


if __name__ == "__main__":
    unittest.main()
