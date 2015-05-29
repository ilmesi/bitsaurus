from lib.address import BitcoinAddress


if __name__ == '__main__':
    private = 0xA0DC65FFCA799873CBEA0AC274015B9526505DAAAED385155425F7337704883E
    btc_address = BitcoinAddress(private)
    print btc_address.public