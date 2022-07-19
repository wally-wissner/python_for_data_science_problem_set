import numpy as np


def max_abs_sort(iterable):
    return sorted(iterable, key=lambda values: max(abs(value) for value in values))


if __name__ == "__main__":
    np.random.seed(0)
    iterable = list(np.random.randn(20, 3))
    for i in max_abs_sort(iterable):
        print(i)
