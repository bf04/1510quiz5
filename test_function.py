import unittest
from function import is_sorted


class test_is_sorted(unittest.TestCase):
    def test_in_order(self):
        self.assertTrue(is_sorted([5, 6, 7, 8, 9]))
        self.assertTrue(is_sorted([-5, -3, -1, 2]))

    def test_if_not_in_ascending_order(self):
        self.assertFalse(is_sorted([20, 19, 18, 17, 16]))
        self.assertFalse(is_sorted([10, 9, 8, 7, 6]))

    def test_floats_in_ascending_order(self):
        self.assertTrue(is_sorted([5.0, 6.0, 7.0, 8.0, 9.0]))
        self.assertTrue(is_sorted([-5.0, -3.6, -1.8, 2.2]))

    def test_floats_in_order(self):
        self.assertTrue(is_sorted([5.0, 6.0, 7.0, 8.0, 9.0]))
        self.assertTrue(is_sorted([-5.0, -3.6, -1.8, 2]))

