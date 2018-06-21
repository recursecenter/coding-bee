
# original problems
def easy_sum(a, b):
    """Takes two numbers and returns their sum"""
    return a + b

def easy_product(a, b):
    """Takes two numbers and returns their product"""
    return a * b

def easy_concat(a, b):
    """Takes two strings and returns their concatenation"""
    return a + b

def easy_emptylist(l):
    """Takes a list and returns True for empty list, False for nonempty"""
    return not l

def easy_iseven(x):
    """Takes a number and returns True if it's even, otherwise False"""
    return x % 2 == 0

def easy_and(b1, b2):
    "Takes two booleans and returns their AND"
    return b1 and b2

def easy_or(b1, b2):
    """Takes two booleans and returns their OR"""
    return b1 or b2

def easy_lt(a, b):
    """Takes two numbers and return whether num1 is less than num2"""
    return a < b
    
# new sp2 2018
def easy_contains(a, b):
    """Takes in 2 non-empty strings and returns True if the first value contains a substring that matches the second value."""
    return b in a

def easy_helloname(a):
    """Takes in a string representing a name and returns a new string saying hello in a very specific format, e.g., if the name is 'Dave', it should return 'Hello, Dave!'"""
    return 'Hello, {}!'.format(a)

def easy_iscat(a):
    """Takes in a string and returns 'meow' if it is the exact string 'cat', otherwise 'woof'."""
    return 'meow' if a == 'cat' else 'woof'
