def bank():
    n = int(input("enter a number: "))
    years = int(input("enter the year: "))

    proc = 1 / 10
    money = n * proc

    i = 0

    while i < years:
        n += money
        i += 1

    print(round(n, 2))


print(bank())