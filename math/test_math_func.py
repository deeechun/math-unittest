import unittest

"""These import the functions from math_func in the same directory"""
from math_func import (
	add,
	subtract,
	multiply,
	divide
	)


class Test_math_func(unittest.TestCase):

	"""This test uses two arguments (2 and 3) in the add function and expects to see an output of 5"""
    def test_add(self):
    	added_value = add(2,3)
    	expected_value = 5
    	self.assertEqual(added_value, expected_value)

    """This test uses two arguments (2 and 3) in the subtract function and expects to see an output of -1"""
    def test_subtract(self):
    	subtracted_value = subtract(2,3)
    	expected_value = -1
    	self.assertEqual(subtracted_value, expected_value)

    """This test uses two arguments (2 and 3) in the multiply function and expects to see an output of 6"""
    def test_multiply(self):
    	multiplied_value = multiply(2,3)
    	expected_value = 6
    	self.assertEqual(multiplied_value, expected_value)

    """This test uses two arguments (4 and 2) in the divide function and expects to see an output of 2"""
    def test_divide(self):
    	divided_value = divide(4,2)
    	expected_value = 2
    	self.assertEqual(divided_value, expected_value)

"""This part of the file will only run if run as a script, not as an import"""
"""This command will run the unit tests present in this file"""
if __name__ == '__main__':
	unittest.main()