def gcd(a,b):
    if a <=0 or b <=0:
        print("Only use positive values")
    else:
        if a > b:
            tmp = a
            a = b
            b = tmp
        remainder = b % a
        while remainder > 0 :
            b = a
            a = remainder
            remainder = b % a
        return a


## https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

    
from typing import Tuple
def xgcd(a: int, b: int) -> Tuple[int, int, int]:
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0    


xgcd(42823,6409)
gcd(42823,6409)
gcd(2818,769)
gcd(769,2818)
xgcd(769,1200)

modinv(769,1200)
