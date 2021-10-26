def main(n, m):
    list_ = []
    for i in range(n, m+1, 1):
        list_.append(i**2)

    return list_


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    print(main(n, m))
    pass
