if __name__ == "__main__":
    # постарайтесь не использовать "магические" числа,
    # а по возможности дать переменным осмысленные названия и использовать их
    # TODO Распечатать строку лесенкой
    n = int(input())
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, sep='', end='')
        print()