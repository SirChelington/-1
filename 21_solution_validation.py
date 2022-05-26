"""
Solution validation
The aim of this challenge is to write code that can analyze code submissions.
We'll simplify things a lot to not make this too hard.

Write a function named validate that takes code represented as a string as its only parameter.

Your function should check a few things:

the code must contain the def keyword
otherwise return "missing def"
the code must contain the : symbol
otherwise return "missing :"
the code must contain ( and ) for the parameter list
otherwise return "missing paren"
the code must not contain ()
otherwise return "missing param"
the code must contain four spaces for indentation
otherwise return "missing indent"
the code must contain validate
otherwise return "wrong name"
the code must contain a return statement
otherwise return "missing return"
If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.
"""

### my solution
"""

string = "validate('def    return  foo():\n print(123)')"

wanted_list = ["def", ":", "(", ")", "    ", "validate", "return"]
not_wanted_list = ["()"]


def validate(string):
    # vermisste strings im code
    for word in wanted_list:
        if word not in string:
            if word == "validate":
                return "wrong name"

            elif word == "(" or word == ")":
                return "missing paren"

            elif word == "    ":
                return "missing indent"

            else:
                return "missing {}".format(word)

    # ungewünschte strings im code:
    for word in not_wanted_list:
        if word in string:
            if word == "()":
                return "missing param"
            else:
                return "not wanted {}".format(word)

    return True


print(validate(string))
"""

### my solution for the HP

string = "def(sausage):    print(" "hmmm delicious" ")"


def validate(string):
    if "def" not in string:
        return "missing def"

    if ":" not in string:
        return "missing :"

    if "(" and ")" not in string:
        return "missing paren"

    if "(" + ")" in string:
        return "missing param"

    if "    " not in string:
        return "missing indent"

    if "validate" not in string:
        return "wrong name"

    if "return" not in string:
        return "missing return"

    return True


print(validate(string))


### example solution

"""
def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" not in code or ")" not in code:
        return "missing paren"
    if "(" + ")" in code:
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    return True
    """