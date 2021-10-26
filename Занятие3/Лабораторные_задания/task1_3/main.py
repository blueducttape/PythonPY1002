def prime_numbers(n):
    i = 2
    prime_list = []
    while i * i <= n:
        while n % i == 0:
            prime_list.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        prime_list.append(n)
    return prime_list


if __name__ == "__main__":
    print("Введите число: ")
    n = int(input())
    print(prime_numbers(n))
    pass
