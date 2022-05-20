"""
All equal
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
"""

### my solution

awesome_list1 = [2, 3, 4, 5]
awesome_list2 = [2, 2, 2, 2, 2]
awesome_list3 = []


def all_equal(awesome_list):
    if awesome_list == []:
        return True
    else:
        return len(awesome_list) == awesome_list.count(awesome_list[0])


print(all_equal(awesome_list3))


### example solution

"""
# naive solution
def all_equal(items):
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                return False
    return True


# one-liner with nested list comprehension
# and the all() built-in
def all_equal(items):
    return all(item1 == item2 for item1 in items for item2 in items)
"""
