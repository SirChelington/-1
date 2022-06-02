"""
Convert radians into degrees
Write a function in Python that accepts one numeric parameter.
This parameter will be the measure of an angle in radians.
The function should convert the radians into degrees and then return that value.

While you might find a Python library to do this for you, you should write the function yourself.
One hint you get is that you'll need to use Pi in order to solve this problem.
You can import the value for Pi from Python's math module.
"""

### my solution

# Ein Grad entspricht π/180 Radiant.


from cmath import pi
from math import degrees, radians


def convert_radians(radian):
    return radian * (180 / pi)


print(convert_radians(1))

# test
def test(r):
    return degrees(r)


print(test(1))
