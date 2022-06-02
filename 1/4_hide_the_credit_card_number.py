"""
Hide the credit card number
Write a function in Python that accepts a credit card number.
It should return a string where all the characters are hidden with an asterisk except the last four.
For example, if the function gets sent "4444444444444444", then it should return "4444".
"""


### my solution


def credit_card_number(number):
    asterisk = len(number) - 4
    result = asterisk * "*" + number[-4:]
    return result


print(credit_card_number("34586754867900786543678901234"))
