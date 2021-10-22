wind = int(input())

if 1 <= wind <= 4:
    print("Слабый")
elif 4 < wind <= 10:
    print("Умеренный")
elif 10 < wind <= 18:
    print("Сильный")
elif wind > 18:
    print("Ураганный")
