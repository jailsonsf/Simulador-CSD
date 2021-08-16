from app.base_converter.converter import Converter


bases = {
    1: 'Base 2',
    2: 'Base 8',
    3: 'Base 10',
    4: 'Base 16'
}


class Base_converter:
    def __init__(self) -> None:
        self.get_original_base()
        self.get_base_to_converter()
        self.get_value()
        self.converter()

    def show_bases(self) -> None:
        for key in bases:
            print(f'[{key}] - {bases[key]}')

    def get_original_base(self) -> None:
        print(f'Selecione a base numérica original')
        self.show_bases()

        option = int(input('>>> '))

        if option not in bases.keys():
            print(f'Opção inválida!')

        else:
            self.original_base = bases[option]

    def get_base_to_converter(self) -> None:
        print(f'Selecione a base numérica para qual deseja converter:')
        self.show_bases()

        option = int(input('>>> '))

        if option not in bases.keys():
            print(f'Opção inválida!')

        else:
            self.base_to_converter = bases[option]

    def get_value(self) -> None:
        print(f'Digite o valor na {self.original_base}:')
        self.value = input('>>> ')

    def converter(self) -> None:
        converter = Converter()

        if self.original_base == self.base_to_converter:
            print(f'Selecione bases diferentes!')

        if self.original_base == 'Base 10':
            if self.base_to_converter == 'Base 2':
                self.result = converter.dec2bin(int(self.value))
                print(
                    f'{self.value} na base {self.original_base}, corresponde a {self.result} na base {self.base_to_converter}')

            elif self.base_to_converter == 'Base 8':
                self.result = converter.dec2oct(int(self.value))
                print(
                    f'{self.value} na base {self.original_base}, corresponde a {self.result} na base {self.base_to_converter}')

            elif self.base_to_converter == 'Base 16':
                self.result = converter.dec2hex(int(self.value))
                print(
                    f'{self.value} na base {self.original_base}, corresponde a {self.result} na base {self.base_to_converter}')

        elif self.original_base == 'Base 2':
            if self.base_to_converter == 'Base 10':
                self.result = converter.bin2dec(self.value)
                print(
                    f'{self.value} na base {self.original_base}, corresponde a {self.result} na base {self.base_to_converter}')

            elif self.base_to_converter == 'Base 8':
                base_10 = converter.bin2dec(self.value)
                self.result = converter.dec2oct(base_10)

                print(
                    f'{self.value} na base {self.original_base}, corresponde a {self.result} na base {self.base_to_converter}')

            elif self.base_to_converter == 'Base 16':
                base_10 = converter.bin2dec(self.value)
                self.result = converter.dec2hex(base_10)

                print(
                    f'{self.value} na base {self.original_base}, corresponde a {self.result} na base {self.base_to_converter}')

        elif self.original_base == 'Base 8':
            if self.base_to_converter == 'Base 10':
                self.result = converter.oct2dec(self.value)
                print(
                    f'{self.value} na base {self.original_base}, corresponde a {self.result} na base {self.base_to_converter}')

            elif self.base_to_converter == 'Base 2':
                base_10 = converter.oct2dec(self.value)
                self.result = converter.dec2bin(base_10)

                print(
                    f'{self.value} na base {self.original_base}, corresponde a {self.result} na base {self.base_to_converter}')

            elif self.base_to_converter == 'Base 16':
                base_10 = converter.oct2dec(self.value)
                self.result = converter.dec2hex(base_10)

                print(
                    f'{self.value} na base {self.original_base}, corresponde a {self.result} na base {self.base_to_converter}')

        elif self.original_base == 'Base 16':
            if self.base_to_converter == 'Base 10':
                self.result = converter.hex2dec(self.value)
                print(
                    f'{self.value} na base {self.original_base}, corresponde a {self.result} na base {self.base_to_converter}')

            elif self.base_to_converter == 'Base 2':
                base_10 = converter.hex2dec(self.value)
                self.result = converter.dec2bin(base_10)

                print(
                    f'{self.value} na base {self.original_base}, corresponde a {self.result} na base {self.base_to_converter}')

            elif self.base_to_converter == 'Base 8':
                base_10 = converter.hex2dec(self.value)
                self.result = converter.dec2oct(base_10)

                print(
                    f'{self.value} na base {self.original_base}, corresponde a {self.result} na base {self.base_to_converter}')
