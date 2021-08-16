from app.base_converter.converter import Converter


class BinarySum:
    def __init__(self) -> None:
        self.get_input()
        self.bin_sum(self.first_value, self.second_value)

    def get_input(self) -> None:
        print('Digite os dois valores de entrada:')
        print('>>> ', end='')
        self.first_value, self.second_value = map(str, input().split())

    def bin_sum(self, number1, number2) -> None:
        converter = Converter()

        number1 = converter.bin2dec(number1)
        number2 = converter.bin2dec(number2)
        result = converter.dec2bin(number1 + number2)

        print(result)
