"""
Just the numbers
Write a function in Python that accepts a list of any length that
contains a mix of non-negative integers and strings.
The function should return a list with only the integers in the original list in the same order.
"""

### my solution

the_list = ["hello", 1, 2, 3, 4, 5, "ah", "oh", 6, 7, 8, 9]


def sort_list_positive_integers(list):
    new_list = []
    for item in list:
        if isinstance(item, int):
            new_list.append(item)
    return new_list


print(sort_list_positive_integers(the_list))
