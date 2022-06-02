"""
Count the vowels in a string
Create a function in Python that accepts a single word and returns the number of vowels in that word.
In this function, only a, e, i, o, and u will be counted as vowels — not y.
"""

### my solution

from itertools import count


def count_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    counter = 0
    result = 0
    for vowel in vowels:
        counter = word.count(vowel)
        result += counter
    return result


print(count_vowels("hausgeist"))
