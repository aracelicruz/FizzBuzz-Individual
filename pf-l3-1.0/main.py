def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Fizzbuzz"   # en el test esperan "Fizzbuzz" con b minúscula
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def main():
    for i in range(1, 1001):  # del 1 al 1000 inclusive
        print(fizzbuzz(i))


if __name__ == "__main__":
    main()
