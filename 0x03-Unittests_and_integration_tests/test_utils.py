#!/usr/bin/python3
import utils
import unittest
from parameterized import parameterized


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
