from RSA.utils import is_prime, find_e, randint, karatsuba, modinv, gcd
from RSA.Decrypting import getting_private_key, decrypting_method, getting_massage
from RSA.Encrypting import getting_public_key, encrypting_method

import os


def encrypting_data():
    """encrypting data with pulic key"""
    public_key, text = getting_public_key("new_text.txt", "public_key.txt")
    encrypted_text = encrypting_method(text, public_key)

    store = '\n'.join([str(elem) for elem in encrypted_text])
    store = store.replace("['", "")
    store = store.replace("']", "")
    store = store.replace("', '", " ")
    with open("encrypted_text.txt", "w") as text_file:
        text_file.write(store)


def decrypting():
    """decrypting data with private key"""
    private_key, encrypted_text = getting_private_key()
    text_code = decrypting_method(encrypted_text, private_key)

    text = getting_massage(text_code)

    with open("decrypted_text.txt", "w") as text_file:
        text_file.write(text)


def generating_keys(result_path=''):
    """
    generating public and private key files
    all calculation uses optimized methods
    """
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

    public_key_path = os.path.join(result_path, "public_key.txt")
    private_key_path = os.path.join(result_path, "private_key.txt")

    with open(public_key_path, "w") as text_file:
        text_file.write(str(public_key[0]) + " " + str(public_key[1]))
    with open(private_key_path, "w") as text_file:
        text_file.write(str(private_key[0]) + " " + str(private_key[1]) + " " + str(private_key[2]) + " " + str(
            private_key[3]) + " " + str(private_key[4]) + " " + str(private_key[5]) + " " + str(private_key[6]))


if __name__ == "__main__":
    generating_keys()
    encrypting_data()
    decrypting()
