def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


if __name__ == "__main__":
    print(factorial(3))
    pass
