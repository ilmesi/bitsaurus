

def egcd(a, b):
    """
    Extended Euclidean Algorithm
    http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    http://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    """
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modular_inverse(a, m):
    """
    Used for division in elliptic curves. Very important in RSA/ECDSA algorithms.
    It uses EGCD 
    """
    gcd, x, y = egcd(a, m)
    return x % m