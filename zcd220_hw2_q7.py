def findChange(lst01):
    i = 0
    j = len(lst01) - 1
    while i < j:
        m = (i + j) // 2
        if lst01[m] == 0:
            i = m + 1
        elif lst01[m] == 1:
            if lst01[m - 1] == 0:
                return m
            else:
                j = m
