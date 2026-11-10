n = int(input())

if n < 2:
    print("Ошибка")
else:
    divisor = 2
    first = True
    while n > 1:
        if n % divisor == 0:
            if not first:
                print(" ", end="")
            print(divisor, end="")
            first = False
            n = n // divisor
        else:
            divisor += 1
    print()

