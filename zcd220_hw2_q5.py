def split_parity(lst):
    odd = 0
    even = len(lst) - 1

    while odd < even:
        if lst[odd] % 2 == 0:
            lst[odd], lst[even] = lst[even], lst[odd]
            even -= 1
        else:
            odd += 1
