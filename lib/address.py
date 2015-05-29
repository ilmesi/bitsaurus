from ECC import Secp256k1


class BitcoinAddress(object):

    def __init__(self, private):
        self.private = private
        self._generate()

    def _generate(self):
        self.public = Secp256k1.multiply(self.private)