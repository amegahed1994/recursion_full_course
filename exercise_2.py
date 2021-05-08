"""
Exercise 2:
Give an array 'arr' and integer 'num', create a recursive function that returns the
num of occurences of 'num' in 'arr'
"""


def num_of_occurences(num, arr):
    if not arr:
        return 0

    elif arr[0] == num:
        return 1 + num_of_occurences(num, arr[1:])

    else:
        return num_of_occurences(num, arr[1:])


if __name__ == "__main__":
    num = 3
    arr = [3, 1, 2, 3, 3]

    print(num_of_occurences(num, arr))
