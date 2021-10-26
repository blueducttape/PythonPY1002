def main():
    i = int(input())
    list_ = []
    while i >=0 :
        if i in range(3, 14):
            list_.append(i)
        i = int(input())
    return list_


if __name__ == "__main__":
    print(main())
    pass
