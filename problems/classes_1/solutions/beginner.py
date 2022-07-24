class Complex(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __repr__(self):
        return f"Complex({self.a}, {self.b})"


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
