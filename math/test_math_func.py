import unittest

# These import the functions from math_func in the same directory
# being more explicit, verbose, and ordered alphabetically.
from math_func import add
from math_func import divide
from math_func import multiply
from math_func import subtract


class Test_math_func(unittest.TestCase):

    # this method is called for every test case create and removed
    # the repetition of calling a function multiple times.
    def _callFUT(self, x, y):
        """
            Calls the function under test and returns the 
            value for checking against the expected value.
        """
        return add(x, y)

    # Looking at the docstrings written in the implementation
    # create test cases.
    def test_add_positive_floats_is_valid(self):
        """
            Given two positive numbers we expect the function
            to return a positive floating number.
        """
        test_positive_x = 5.4
        test_positive_y = 2.6

        # call the function under test and get back a value
        returned_value = self._callFUT(
                            test_positive_x,
                            test_positive_y
                        )
        # what we expect to be returned based off the parameters
        # that were passed in.
    	expected_return = 14.04 

    	self.assertEqual(returned_value, expected_value)

    def test_add_negative_floats_is_valid(self):
        """
            Given two negative numbers we expect the function
            to return a negative number.
        """
        raise NotImplemented


class Test_math_func_subtract(unittest.TestCase):
    """ All test cases for the subtraction function."""

    def _callFUT(self, x, y):
        """ Call the function under test. """
        return subtract(x, y)

    def test_subtract_positive_floats_is_valid(self):
        raise NotImplemented


class Test_math_func_multiply(unittest.TestCase):
    """ All tests cases for the multiply function. """

    def _callFUT(self, x, y):
        """ Calls the function under test. """
        return multiply(x, y)

    def test_multiply_positive_float_is_valid(self):
        raise NotImplemented

class Test_math_func_divide(unittest.TestCase):
    """ All test cases for the divide function. """

    def _callFUT(self, x, y):
        """ Calls the function under test. """
        return divide(x, y)

    def test_divide_positive_float_is_valid(self):
        raise NotImplemented

    def test_divide_returns_undefine(self):
        raise NotImplemented

    def test_divide_negative_float_is_valid(self):
        raise NotImplemented 

# This part of the file will only run if run as a script, not as an 
# import This command will run the unit tests present in this file
if __name__ == '__main__':
	unittest.main()