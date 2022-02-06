def karatsuba(x, y):
    """Karatsuba method for fast multiplication"""
    if x < 10 and y < 10:
        return x * y

    num1_len = len(str(x))
    num2_len = len(str(y))

    n = max(num1_len, num2_len)

    # round decides to be floor or ceil value
    # by this we can reduce some function calls
    # of ceil or floor recursively

    nby2 = round(n / 2)

    num1 = x // (10 ** nby2)
    rem1 = x % (10 ** nby2)

    num2 = y // (10 ** nby2)
    rem2 = y % (10 ** nby2)

    ac = karatsuba(num1, num2)
    bd = karatsuba(rem1, rem2)
    ad_plus_bc = karatsuba(num1 + rem1, num2 + rem2) - ac - bd

    return (10 ** (2 * nby2)) * ac + (10 ** nby2) * ad_plus_bc + bd
