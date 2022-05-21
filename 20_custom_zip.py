"""
Custom zip
The built-in zip function "zips" two lists. Write your own implementation of this function.

Define a function named zap. The function takes two parameters, a and b. These are lists.

Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.

You may assume a and b have equal lengths.

If you don't get it, think of a zipper.

For example:

zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
)
Should return:

[(0, 5),
 (1, 6),
 (2, 7),
 (3, 8)]
"""

### my solution

list_a = [0, 2, 4, 6]
list_b = [1, 3, 5, 7]


def zap(list_a, list_b):
    new_list = []
    for item in range(len(list_a)):
        temporary_tuple = list_a[item], list_b[item]
        new_list.append(temporary_tuple)
    return new_list


print(zap(list_a, list_b))


### example solution

"""
# ugly but understandable solution
def zap(a, b):
    result = []
    for i in range(len(a)):
        item_from_a = a[i]
        item_from_b = b[i]
        tup = (item_from_a, item_from_b)
        result.append(tup)
    return result

# concise solution with list comprehensions
def zap(a, b):
    return [(a[i], b[i]) for i in range(len(a))]
"""
