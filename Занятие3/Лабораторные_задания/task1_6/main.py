def main(month_price, inflation):
    average_ = []
    month_with_infl = month_price*inflation
    for i in range (10):
        average_.append(month_with_infl)
        month_with_infl*=inflation

    return average_


if __name__ == "__main__":
    aver_stip = 10000*10
    month_price = 12000
    inflation = 1.03
    aver_price = (sum (main(month_price, inflation)))
    print(aver_price)
    print (aver_stip - aver_price)
    pass
