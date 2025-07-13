import unittest

from main import is_even, is_odd, add, subtract, multiply, divide

class mathfunctions(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
    
    def test_is_odd(self):
        self.assertTrue(is_odd(5))
        self.assertFalse(is_odd(4))
    
    def test_add(self):
        self.assertEqual(add(3,4), 7)
    def test_subtract(self):
        self.assertEqual(subtract(5,3), 2)
    
    def test_multiply(self):
        self.assertEqual(subtract(2,2), 4)
    
    def test_devide(self):
        self.assertEqual(subtract(6,3), 2)

        