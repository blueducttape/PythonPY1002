def long_word():
    s = input()
    s = s.split()
    n =(max(s, key=len))
    reverse = n[::-1]
    return reverse


if __name__ == "__main__":
    print(long_word())
    pass
