import math


def taylor_exp(x, n):
    t = 0.0
    result = 0
    for i in range(0, n+1):
        m = (pow(x, i)) / math.factorial(i)
        result += m
    return result


def geometric_series_sum(s, e, q):
    if q == 1:
        return e - s + 1
    else:
        return pow(q, s) * (1 - pow(q, (e - s + 1))) / (1 - q)
