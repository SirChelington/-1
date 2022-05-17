"""
Flatten a list
Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function flatten. It should take a single parameter and return a list.

For example, calling:

flatten([[1, 2], [3, 4]])
Should return the list:

[1, 2, 3, 4]
"""

### my solution
def flatten(lists):
    flatten_list = []
    for count in range(len(lists)):
        for item in lists[count]:
            flatten_list.append(item)
    return flatten_list


lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(flatten(lists))


### example solution
"""
# naive solution
def flatten(outer_list):
    result = []
    for inner_list in outer_list:
        for item in inner_list:
            result.append(item)
    return result

# solution with nested list comprehensions
# (can be put on a single line for conciseness)
def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]
"""
