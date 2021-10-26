def task(str1, str2, k):
    str1 = input()
    str2 = input()
    k = str1[1]
    if k == str2[1]:
        print("ДА")
    else:
        print("НЕТ")


if __name__ == "__main__":
    print(task())
