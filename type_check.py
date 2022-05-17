"""Type check
Write a function named only_ints that takes two parameters.
Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
"""

from xmlrpc.client import boolean


def only_ints(one, two):
    if (
        isinstance(one, int)
        and isinstance(two, int)
        and not isinstance(two, boolean)
        and not isinstance(one, boolean)
    ):
        return True
    else:
        return False


print(only_ints(9, True))

def only_ints2(a, b):
    return type(a) == int and type(b) == int

print(only_ints2(9, True))
