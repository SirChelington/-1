"""
6. Are the Xs equal to the Os?
Create a Python function that accepts a string.
This function should count the number of Xs and the number of Os in the string.
It should then return a boolean value of either True or False.

If the count of Xs and Os are equal, then the function should return True.
If the count isn't the same, it should return False.
If there are no Xs or Os in the string, it should also return True because 0 equals 0.
The string can contain any type and number of characters.
"""


### my solution

from itertools import count


def count_x_and_o(string):
    count_x = string.count("x") + string.count("X")
    count_o = string.count("o") + string.count("O")
    if count_x == count_o:
        return True
    else:
        return False


print(count_x_and_o("test X x x x o o o O"))
