def e_approx(n):
    e = 1
    denom = 1
    for i in range(1, n + 1):
        denom = denom * i
        e += 1 / denom

    return e
