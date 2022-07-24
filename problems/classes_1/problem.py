"""
Complex numbers are numbers of the form a + i * b where i is the square root of -1. They have the following properties:
Given z1 = a1 + i * b1 and z2 = a2 + i * b2 then:
    Addition:       z1 + z2 = (a1 + a2) + i * (b1 + b2)
    Multiplication: z1 * z2 = (a1 * a2 - b1 * b2) + i * (a1 * b2 + a2 * b1)

Classes are a way to create new Python objects. Numbers, lists, and functions are all objects defined by classes.
Create a class that implements complex numbers.
"""


class Complex(object):
    def __init__(self, a, b):
        ...

    def __add__(self, other):
        ...

    def __mul__(self, other):
        ...

    def __eq__(self, other):
        ...

    def __repr__(self):
        ...


if __name__ == "__main__":
    z1 = Complex(1, -5)
    z2 = Complex(1, 5)
    print(z1)
    print(z2)
    print(z1 + z2)
    print(z1 * z2)
    print(z1 * (z1 + z2))
    assert z1 + z2 == Complex(2, 0)
    assert z1 * z2 == Complex(26, 0)
    assert z1 * (z1 + z2) == Complex(2, -10)
