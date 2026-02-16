
D, C, P = list(map(int, input().split(' ')))
price  = list(map(int, input().split(' ')))

for i in range(D):
    bought = False
    compare_price = price[i]
    last_price =
    if P < compare_price:
        print("WAIT")
    elif P > compare_price:
        print(f"BUY {C // compare_price}")
        money_left = C % compare_price
        bought = True
    elif P == compare_price:
        if bought:
            print("HOLD")
        elif not bought:
            print("WAIT")
        else:



