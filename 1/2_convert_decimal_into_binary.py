"""
Convert a decimal number into binary
Write a function in Python that accepts a decimal number and returns the equivalent binary number.
To make this simple, the decimal number will always be less than 1,024,
so the binary number returned will always be less than ten digits long.
"""


### my solution


def convert_decimal(number):
    return int(bin(number)[2:])

print(convert_decimal(10))
