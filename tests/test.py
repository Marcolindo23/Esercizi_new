import unittest
from calc import Calculations

class TestCalc(unittest.TestCase):
    def test_sum(self):
        calc_1 = Calculations(a=2, b=3)
        result = calc_1.get_sum()
        self.assertEqual(result, 2+3, msg=f"Error Test Failed {result}")
    def test_diff(self):
        calc_1 = Calculations(a=2, b=3)
        result = calc_1.get_difference()
        self.assertEqual(result, 2-3, msg=f"Error Test Failed {result}")
    def test_prod(self):
        calc_1 = Calculations(a=2, b=3)
        result = calc_1.get_product()
        self.assertEqual(result, 2*3, msg=f"Error Test Failed {result}")
    def test_quotient(self):
        calc_1 = Calculations(a=2, b=3)
        result = calc_1.get_quotient()
        self.assertEqual(result, 2/3, msg=f"Error Test Failed {result}")

    
if __name__ == "__main__":
    unittest.main()
