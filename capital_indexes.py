"""Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string.
Your function should return a list of all the indexes in the string that have capital letters.
For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4]."""

import re

capital_indexes_list = []
word = "kAesE"


def capital_indexes(word):
    for i in range(len(word)):
        if re.search(r"[A-Z]+", word[i]):
            capital_indexes_list.append(i)
    return capital_indexes_list


print(capital_indexes(word))
