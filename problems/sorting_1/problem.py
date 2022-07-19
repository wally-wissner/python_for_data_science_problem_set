"""
Given a list of arrays, sort the list by the largest absolute value of the array. For example, array a = (-2, 0, -1)
and array b = (-1, 1, 0), the function should return [b, a] because a has largest absolute value 2 and b has largest
absolute value 1.
"""


import numpy as np


def max_abs_sort(iterable):
    ...


if __name__ == "__main__":
    np.random.seed(0)
    iterable = list(np.random.randn(20, 3))
    for i in max_abs_sort(iterable):
        print(i)
