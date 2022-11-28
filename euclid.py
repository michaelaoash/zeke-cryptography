## Euclidean algorithm
## https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
## Find GCD(a,b) AND find x,y s.t. GCD(a,b) = x*a + y*b
## If GCD(a,b) = 1, then x is the modular multiplicative inverse of a mod b


## I wrote this
def gcd(a,b):
    if a <=0 or b <=0:
        print("Only use positive values")
    else:
        remainder = b % a
        while remainder > 0 :
            b = a
            a = remainder
            remainder = b % a
        return a

## These more sophisticated approaches are from wikibooks
## https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
## Iterative approach 
from typing import Tuple


def xgcd(a: int, b: int) -> Tuple[int, int, int]:
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    ## if gcd(a,b) = 1, then x is the modular multiplicative inverse of a mod b, i.e., ax = 1 mod b
    ## x0 will be the "count" of a's, y0 will be the "count" of b's
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0    


## Recursive approach
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

gcd(6409,42823)
gcd(769,2818)
gcd(769,1200)


xgcd(6409,42823)
xgcd(769,2818)
xgcd(769,1200)

