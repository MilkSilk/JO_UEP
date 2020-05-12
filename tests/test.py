import unittest
from fractions import Fraction

from my_sum import sum123

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Tests that it can sum a list of integers
        :return:
        """
        data = [1, 2, 3]
        result = sum123(data)
        self.assertEqual(result, 6)
        print("Chyba sie udalo!")

    def test_list_fraction(self):
        data = [Fraction(1,4), Fraction(1,4), Fraction(2, 5)]
        result = sum123(data)
        self.assertEqual(result, 1)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum123(data)