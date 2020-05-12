import unittest
from unittest.mock import MagicMock

from my_sum.ProductionClass import ProductionClass

production_class = ProductionClass()

class MyTestCase(unittest.TestCase):

    def test_complex_function(self):
        production_class = ProductionClass()
        production_class.intermediate_function = MagicMock(return_value=2)

        self.assertEqual(4, production_class.complex_function())