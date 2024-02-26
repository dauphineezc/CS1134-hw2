def factors(num):
    yield 1
    sqrt_num = int(num**(1 / 2))

    for i in range(2, sqrt_num):
        if num % i == 0:
            yield i

    if sqrt_num ** 2 == num:
        yield sqrt_num

    for i in range(sqrt_num - 1, 0, -1):
        if num % i == 0:
            yield num // i
