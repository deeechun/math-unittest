import unittest
from math_func import (
	add,
	subtract,
	multiply,
	divide
	)

#Create a class that inherits from TestCase class from unittest package
class Test_math_func(unittest.TestCase):

    def test_add(self):
    	added_value = add(2,3)
    	expected_value = 5
    	self.assertEqual(added_value, expected_value)

    def test_subtract(self):
    	subtracted_value = subtract(2,3)
    	expected_value = -1
    	self.assertEqual(subtracted_value, expected_value)

    def test_multiply(self):
    	multiplied_value = multiply(2,3)
    	expected_value = 6
    	self.assertEqual(multiplied_value, expected_value)

    def test_divide(self):
    	divided_value = divide(4,2)
    	expected_value = 2
    	self.assertEqual(divided_value, expected_value)

#Only run if ran, not imported
if __name__ == '__main__':
	unittest.main()