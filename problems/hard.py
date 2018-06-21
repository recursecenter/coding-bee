
# original problems

def hard_sort_magnitude(l):
    """Takes a list of positive and negative numbers, and sorts them according to their absolute values. The list [3, -2, 1] would normally get sorted to [-2, 1, 3], but we want you to return [1, -2, 3] instead. protip: python's default sort order is ascending"""
    return sorted(l, key=abs)

def hard_merge_dicts(d1, d2):
    """Takes in two dictionaries and returns a dictionary containing entries from the two dictionaries. If a key conflicts, the second dictionary should override the first dictionary. This method should not mutate the input dictionaries."""
    ans = {}
    for k, v in d1.items():
        ans[k] = v
    for k, v in d2.items():
        ans[k] = v
    return ans

def hard_dedupe(s):
    """Takes in a string, and returns a string where only the first occurrence of each letter is retained. So the string 'abccba' goes to 'abc'. The empty string returns the empty string."""
    seen = set()
    ans = ''
    for char in s:
        if char in seen:
            continue
        seen.add(char)
        ans += char
    return ans


def hard_match_parens(s):
    """Takes in a string containing only '()'. Returns True if that string is a valid nesting of parentheses, False otherwise."""
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    if count != 0:
        return False
    return True

# new sp2 2018

def hard_is_palindrome(a):
    """Takes in a string of length 1 or greater and returns True if it is a palindrome."""
    return ''.join(reversed(a)) == a
    
def hard_most_common_letter(a):
    """Takes in a string of lowercase letters and returns the most common letter (if multiple, just pick one)."""
    # too tricky?
    d = {}
    for c in a:
        d[c] = d.get(c, 0) + 1
    l = list(d.items())
    l.sort(key=lambda x: -x[1])
    return l[0][0]

def hard_fizzbuzz():
    """Returns an array of **strings** representing the numbers 1 to 100, but if the number is divisible by 3 replace it with 'fizz' or if the number is divisible by 5 replace it with 'buzz' or if it is divisble by both, replace it with 'fizzbuzz'"""
    return ["fizzbuzz" if i % 3 == 0 and i % 5 == 0 else 
            "fizz" if i % 3 == 0 else 
            "buzz" if i % 5 == 0 else 
            str(i) for i in range(1, 101)]

def hard_num_permutations(a):
    """Takes in a string of non-repeating characters and returns an integer representing the number of permutations of that string."""
    # too tricky?
    return 1 if len(a) < 2 else len(a) * hard_num_permutations(a[1:])

def hard_combine_max(a, b):
    """Takes in 2 lists of integers and returns a new list where each value represents the maxmimum of the input lists at that index. If the lists are not the same length, then the extra values in the longer list should be assumed to be valid maximum values and therefore included in the result."""
    # too tricky?
    z = [max(x, y) for x, y in zip(a, b)]
    if len(a) > len(b):
        z += a[len(b):]
    elif len(b) > len(a):
        z += b[len(a):]
    return z
