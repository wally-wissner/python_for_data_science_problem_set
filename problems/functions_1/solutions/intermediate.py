"""
This solution is more reusable than the beginner solution. It can handle variable divisors, variable replacement text,
and variable separators.
"""


def fizzbuzz(n, replacements, sep):
    if not any(n % r == 0 for r in replacements):
        return n
    else:
        return sep.join(replacements[r] for r in replacements if n % r == 0)


if __name__ == "__main__":
    for n in range(100):
        print(fizzbuzz(n, {3: "Fizz", 5: "Buzz"}, sep=" "))
