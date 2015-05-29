from utils import modular_inverse


class ElitpicCurve(object):

    @classmethod
    def add(cls, a, b):
        return cls.G

    @classmethod
    def double(cls, private):
        return cls.G

    @classmethod
    def multiply(cls, private):
        return cls.G


class Secp256k1(ElitpicCurve):
    """
    Specific Koblitz curve parameters extracted from: http://www.secg.org/sec2-v2.pdf
    Defined by T = (p, a, b, G, n, h)
    Where:
    p: big proven prime
    a: parameter of E: 'y**2 = x**3 + ax + b'
    b: parameter of E: 'y**2 = x**3 + ax + b'
    G(x,y): generator point used for the multiplication step
    n: number of points in the field
    h: cofactor used
    """
    p = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1
    a = 0
    b = 7
    G = (55066263022277343669578718895168534326250603453777594175500187360389116729240, 
         32670510020758816978083085130507043184471273380659243275938904335757337482424)
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    h = 1