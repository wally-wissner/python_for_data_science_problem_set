def fizzbuzz(n):
    if n % 15 == 0:
        return "Fizz Buzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n


if __name__ == "__main__":
    for n in range(100):
        print(fizzbuzz(n))
