import struct
import time

"""Generating random numbers without random function"""


def lastbit(f):
    return struct.pack('!f', f)[-1] & 1


def getrandbits(k):
    result = 0
    for _ in range(k):
        time.sleep(0)
        result <<= 1
        result |= lastbit(time.perf_counter())
    return result


def randint(a, b):
    return a + randbelow(b - a + 1)


def randbelow(n):
    if n <= 0:
        raise ValueError
    k = n.bit_length()
    r = getrandbits(k)
    while r >= n:
        r = getrandbits(k)
    return r
