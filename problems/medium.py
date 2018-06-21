
# original problems
def med_is_hex(s):
    """Takes a string and returns whether all characters of the string are contained within [0123456789abcdef] - assume lowercase abcdef."""
    return set(s) <= set('1234567890abcedf')

def med_is_decimal(s):
    """Takes a string and returns whether all characters of the string are digits."""
    return set(s) <= set('1234567890')

def med_splice_stars(s):
    """Takes a string and returns the same string, but with the asterisk character interwoven with the string. The empty string should return the empty string and a single character should return that character again."""
    return '*'.join(s)

def med_sum_digits(s):
    """Takes a string that contains only digits, and returns the sum of those digits."""
    return sum(map(int, s))

def med_fib(n):
    """Returns the nth fibonacci number. Fib(0) = 0 and Fib(1) = 1 for these purposes."""
    return n if n < 2 else med_fib(n-1) + med_fib(n-2) 

def med_factorial(n):
    """Returns n factorial. Factorial(0) = 1, Factorial(1) = 1."""
    return 1 if n < 2 else n * med_factorial(n-1)

def med_product(l):
    """Takes a list of numbers and returns their product. A list of length 1 should return its sole element, and a list of length 0 should return 1."""
    return 1 if not l else l[0] * med_product(l[1:])

def med_leftpad(s, n):
    """Takes a string and a number (guaranteed to be greater than length of the string), and returns that string, padded on its left side with empty space characters such that the length of the string equals the number."""
    return ' ' * (n - len(s)) + s

# new sp2 2018
def med_all_odd(a):
    """Takes in a non-empty list of integers and returns True if all values are odd in the list."""
    return all(x % 2 == 1 for x in a)

def med_caseinsensitive_equal(a, b):
    """Takes in two strings and returns True if they are case insensitive equal."""
    return a.lower() == b.lower()

def med_min_2darray(a):
    """Takes in a list of lists of integers and returns the minimum value."""
    return min(min(inner) for inner in a)

def med_clamp(a,lo,hi):
    """Takes in 3 integers: a value to clamp, a lo, and a hi, returning the value if it is within the range of lo to hi, otherwise the nearest value of lo or hi."""
    return min(hi, max(lo, a))

def med_array_equal(a,b):
    """Takes in 2 lists containing integers and returns True if they have the same values in the same order."""
    return len(a) == len(b) and all(x == y for x, y in zip(a, b))
