"""
Give me the discount
Create a function in Python that accepts two parameters.
The first should be the full price of an item as an integer.
The second should be the discount percentage as an integer.

The function should return the price of the item after the discount has been applied.
For example, if the price is 100 and the discount is 20, the function should return 80.
"""

### my solution


def discount(full_price, discount_percentage):
    return full_price * ((100 - discount_percentage) / 100)


print(discount(99.99, 7))
