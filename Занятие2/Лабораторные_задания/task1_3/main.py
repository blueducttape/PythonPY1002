a = int(input())
b = int(input())
if a**2 + b**2 > (a+b)**2:
    print("Сумма квадратов больше")
elif a**2 + b**2 < (a+b)**2:
    print("Квадрат суммы больше")
