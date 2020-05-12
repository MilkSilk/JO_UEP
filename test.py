import unittest

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

if __name__ == "__main__":
    unittest.main()