"""
Exercise 1:
Given a positive integer n, create a recursive function that returns the sum of its digits.
"""

# My solution
def sum_of_digits(n):
    if n < 10:
        return n

    n_str = str(n)
    return int(n_str[0]) + sum_of_digits(int(n_str[1:]))

# Answer key
def sum_of_digits(n):
    if n < 10:
        return n

    return n%10 + sum_of_digits(n//10)


if __name__ == "__main__":
    print(sum_of_digits("123"))
