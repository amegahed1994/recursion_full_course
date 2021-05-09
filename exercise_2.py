"""Exercise 2:

Give an array 'arr' and integer 'num', create a recursive function that
returns the num of occurences of 'num' in 'arr'.
"""


# My solution
def num_of_occurences(num, arr):
    if not arr:
        return 0

    elif arr[0] == num:
        return 1 + num_of_occurences(num, arr[1:])

    else:
        return num_of_occurences(num, arr[1:])


# Answer key
def _num_of_occurences(num, arr, index=0):
    if index == len(arr):
        return 0
    elif arr[index] == num:
        return 1 + _num_of_occurences(num, arr, index + 1)
    else:
        return _num_of_occurences(num, arr, index + 1)


if __name__ == "__main__":
    num = 3
    arr = [3, 1, 2, 3, 3]

    assert num_of_occurences(num, arr) == 3
    assert _num_of_occurences(num, arr) == 3
