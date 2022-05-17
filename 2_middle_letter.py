"""Middle letter
Write a function named mid that takes a string as its parameter.
Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return ""."""

### my solution
def mid(string):
    if len(string) % 2 == 0:
        return ""
    else:
        middle_letter = len(string) // 2
        return string[middle_letter]


print(mid("abcaaaaaaagggggPuuuuuoooooaaaaa"))


### example solution
"""
# this approach uses // which is integer division in Python 3
# alternatively, use / and int() in combination.
def mid(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]
"""
