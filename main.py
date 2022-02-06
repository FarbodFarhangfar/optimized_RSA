from extended_euclidean import modinv, gcd
from Karatsuba import karatsuba
from random_generator import randint
from prime import is_prime





def is_coprime(x, y):
    return gcd(x, y) == 1


def find_e(ph, m):
    for i in range(m, ph):
        if is_coprime(i, ph):
            return i




if __name__ == "__main__":
    p = randint(100, 10000)
    q = randint(100, 10000)
    while not is_prime(p):
        p = randint(100, 10000)
    while not is_prime(q):
        q = randint(100, 10000)

    n = karatsuba(p, q)
    phi = karatsuba((p - 1), (q - 1))
    m = max(p, q)

    e = find_e(phi, m)
    e = 17  # pick 3 , 17 or 65537 for faster computing

    d = modinv(e, phi)
    public_key = (e, n)
    dq = pow(d, 1, q - 1)
    dp = pow(d, 1, p - 1)
    qinv = modinv(q, p)
    private_key = (d, n, p, q, dp, dq, qinv)

    with open("public_key.txt", "w") as text_file:
        text_file.write(str(public_key[0]) + " " + str(public_key[1]))
    with open("private_key.txt", "w") as text_file:
        text_file.write(str(private_key[0]) + " " + str(private_key[1]) + " " + str(private_key[2]) + " " + str(
            private_key[3]) + " " + str(private_key[4]) + " " + str(private_key[5]) + " " + str(private_key[6]))
