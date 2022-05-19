"""
Up and down
Define a function named up_down that takes a single number as its parameter.
Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.

For example, calling up_down(5) should return (4, 6).
"""

### my solution


def up_down(number):
    two_numbers_beside = number - 1, number + 1
    return two_numbers_beside


print(up_down(5))


### example solution


"""
def up_down(x):
    return (x-1, x+1)
"""
