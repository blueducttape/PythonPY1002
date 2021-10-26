def infinity (epsilon = 0.0001):
    infinity_list_ = []
    n = 2
    while True:
        i = 1/n
        if i > epsilon:
            infinity_list_.append(i)
            n *= 2
        else:
            break

    return(sum (infinity_list_))


if __name__ == "__main__":
    print (infinity())
    pass
