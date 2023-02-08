"""These are extended function that required for computing"""


def gcd(p, q):
    """greatest common divisor"""
    while q != 0:
        p, q = q, p % q
    return p


def lcm(p, q):
    """Least common multiple"""
    return p * q / gcd(p, q)


def egcd(a, b):
    """extended greatest common divisor"""
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)


def modinv(a, m):
    """modular multiplicative invers"""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m


def chineseremaindertheorem(dq, dp, p, q, qinv, c):
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)

    h = (qinv * (m1 - m2)) % p
    m = m2 + h * q
    return m
