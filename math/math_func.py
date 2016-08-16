"""
	Simple math functions. These functions should only be used with number types
"""

def add(x, y):
"""
	Takes in two arguments and returns the addition of the two

	Args:
		x is any real whole positive integer.
		y is any real whole positive integer.

	Returns:
		The sum of both x and y.
"""
    return x + y

def multiply(x, y):
"""
	Takes in two arguments and returns the multipication of the two

	Args:
		x is any real floating number.
		y is any real floating number.

	Returns:
		Multiplies both x and y.
"""
    return x * y

def divide(x, y):
"""
	Takes in two arguments and returns the division of the 
	first argument by the second argument. For example, divide(6,3) 
	will calculate '6 / 3' and return 2

	Args:
		x is any real floating number.
		y is any real floating number except for zero.

	Note:
		if y is a zero python throws an exception and we will
		print our own message notifying the user as "undefined answer".

	Returns:
		Any floating point value.
"""
    return x / y

def subtract(x, y):
"""
	Takes in two arguments and returns the subtraction of the second
	argument from the first argument. For example, subtract(1,2) will
	calculate '1 - 2' and return -1

	Args:
		x is any real floating number.
		y is any real floating number.

	Returns:
		Either a positive or negative floating number.
"""
    return x - y

