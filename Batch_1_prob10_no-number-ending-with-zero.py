def no_zero():
    for num in range(101):
        if num % 10 == 0:
            continue
        else:
            print(num)
no_zero()