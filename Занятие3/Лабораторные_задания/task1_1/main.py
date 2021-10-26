def main():
    sqr_list_ = []
    count = 0
    while sum(sqr_list_) < 500:
        sqr_list_.append(count**2)
        count += 1
    return len(sqr_list_) - 1


if __name__ == "__main__":
    print(main())
    pass
