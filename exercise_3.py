"""Exercise 2:

Given a string 'str', create a recursive boolean function that checks if
'str' has adjacent duplicates, in other words, if there is a character
that appears two or more times in a row in the string.
"""


def has_adjacent_dups(arr, index=0):
    if index >= len(arr) - 1:
        return False

    elif arr[index] == arr[index + 1]:
        return True
    else:
        return has_adjacent_dups(arr, index + 1)


if __name__ == "__main__":
    arr = [3, 1, 2, 3, 3]

    print(has_adjacent_dups(arr))
