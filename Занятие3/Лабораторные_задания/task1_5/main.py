def sum_list():
    i = int(input())
    list_ = []
    while i != 0:
        if i >0:
            list_.append(i)
        i = int(input())
    return sum(list_)


if __name__ == "__main__":
    print(sum_list())
    pass
