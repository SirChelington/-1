"""
Create a calculator function
Write a Python function that accepts three parameters.
The first parameter is an integer. 
The second is one of the following mathematical operators: +, -, / or *.
The third parameter will also be an integer.

The function should perform a calculation and return the results.
For example, if the function is passed 6 and 4, it should return 24.
"""

### my solution


def calculator(integer1, operator, integer2):
    operator_list = ["+", "-", "*", "/"]
    if (
        isinstance(integer1, int)
        and isinstance(integer2, int)
        and operator in operator_list
    ):
        if operator == "+":
            return integer1 + integer2
        elif operator == "-":
            return integer1 - integer2
        elif operator == "*":
            return integer1 * integer2
        elif operator == "/" and integer2 != 0:
            return integer1 / integer2
        else:
            return "can not divide by zero"
    else:
        return "wrong parameter"


print(calculator(40, "/", 5))
