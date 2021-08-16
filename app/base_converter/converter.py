dec_to_hex = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

hex_to_dec = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}


class Converter:
    def __init__(self) -> None:
        pass

    def dec2bin(self, number: float) -> None:
        result = ''

        while number >= 2:
            rest = str(int(number % 2))
            number = number // 2

            result += rest

        result += str(int(number))

        return result[::-1]

    def bin2dec(self, number: float) -> None:
        list_number = list(str(number))[::-1]

        dec_value = 0
        for i in range(len(list_number)):
            dec_value += int(list_number[i]) * (2**i)

        return dec_value

    def dec2oct(self, number: float) -> None:
        result = ''

        while number >= 8:
            rest = str(int(number % 8))
            number = number // 8

            result += rest

        result += str(int(number))

        return result[::-1]

    def oct2dec(self, number: float) -> None:
        list_number = list(str(number))[::-1]

        dec_value = 0
        for i in range(len(list_number)):
            dec_value += int(list_number[i]) * (8**i)

        return dec_value

    def dec2hex(self, number: float) -> None:
        result = ''

        while number >= 16:
            rest = int(number % 16)
            number = number // 16

            if rest >= 10:
                rest = dec_to_hex[rest]

            result += str(rest)

        result += str(int(number))

        return result[::-1]

    def hex2dec(self, number: float) -> None:
        list_number = list(str(number))[::-1]

        dec_value = 0
        for i in range(len(list_number)):
            if list_number[i].upper() in hex_to_dec:
                dec_value += hex_to_dec[list_number[i].upper()]

            else:
                dec_value += int(list_number[i]) * (16**i)

        return dec_value
