units = {
    1: 'Byte',
    2: 'Kylobyte',
    3: 'Megabyte',
    4: 'Gigabyte',
    5: 'Terabyte'
}


class UnitConverter:
    def __init__(self) -> None:
        self.get_unit_to_provide()
        self.get_unit_to_converter()
        self.get_value()
        self.converter()

    def show_units(self) -> None:
        for key in units:
            print(f'[{key}] - {units[key]}')

    def get_unit_to_provide(self) -> None:
        print(f'Selecione a unidade de medida para qual fornecerá um valor:')
        self.show_units()

        option = int(input('>>> '))

        if option not in units.keys():
            print(f'Opção inválida!')

        else:
            self.unit_provide = units[option]

    def get_unit_to_converter(self) -> None:
        print(f'Selecione a unidade de medida para qual deseja converter:')
        self.show_units()

        option = int(input('>>> '))

        if option not in units.keys():
            print(f'Opção inválida!')

        else:
            self.unit_converter = units[option]

    def get_value(self) -> None:
        print(f'Digite o valor em {self.unit_provide}:')
        self.value = float(input('>>> '))

    def converter(self) -> None:
        for key in units:
            if units[key] == self.unit_provide:
                unit_provide_num = key

            elif units[key] == self.unit_converter:
                unit_converter_num = key

        if self.unit_provide == self.unit_converter:
            print('Selecione unidades diferentes!')

        elif unit_provide_num > unit_converter_num:
            multiplications = abs(unit_provide_num - unit_converter_num)

            print(
                f'{self.value} {self.unit_provide} equivalem a {self.value * (1000**multiplications)} {self.unit_converter}')

        elif unit_provide_num < unit_converter_num:
            divisions = abs(unit_provide_num - unit_converter_num)
            print(
                f'{self.value} {self.unit_provide} equivalem a {self.value / (1000**divisions)} {self.unit_converter}')
