"""Sort a list
Create a function in Python that accepts two parameters.
The first will be a list of numbers. 
The second parameter will be a string that can be one of the following values: asc, desc, and none.
If the second parameter is "asc," then the function should return a list with the numbers in ascending order.
If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered."""

number_list = [2, 4, 1, 3, 6, 5, 9, 8, 7, 0]
command_list = ["ascending", "descending", "none"]


def sorting_list(numbers, sort):
    if sort == "ascending":
        asc_list = sorted(numbers)
        return asc_list

    if sort == "descending":
        desc_list = sorted(numbers, reverse=True)
        return desc_list

    if sort == "none":
        return numbers


for i in range(len(command_list)):
    print(sorting_list(number_list, command_list[i]))