"""
Min-maxing
Define a function named largest_difference that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and smallest number in the list.

For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

You may assume that no numbers are smaller or larger than -100 and 100.
"""

### my solution
numbers = [1, 2, 3, 4, 5]


def largest_difference(number_list):
    sort = sorted(number_list)
    quick_math = sort[-1] - sort[0]
    return quick_math


print(largest_difference(numbers))


### example solution

"""
# short solution
def largest_difference(numbers):
    return max(numbers) - min(numbers)

# naive solution
def largest_difference(numbers):
    smallest = 100
    for n in numbers:
        if n < smallest:
            smallest = n

    largest = -100
    for n in numbers:
        if n > largest:
            largest = n

    difference = largest - smallest
    return difference
"""
