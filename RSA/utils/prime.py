from .extended_euclidean import gcd
from .random_generator import randint




def is_coprime(x, y):
    return gcd(x, y) == 1


def find_e(ph, m):
    for i in range(m, ph):
        if is_coprime(i, ph):
            return i


def is_prime(n, k=128):  #
    """Miller–Rabin primality test"""

    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    for _ in range(k):
        a = randint(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True
