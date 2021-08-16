class Gates:
    def __init__(self) -> None:
        pass

    def not_gate(self, value: int) -> str:
        result = not value

        if result == False:
            return '0'

        elif result == True:
            return '1'

    def or_gate(self, values: list) -> str:
        result = int(values[0])
        for item in values:
            result = result or int(item)

        return result

    def and_gate(self, values: list) -> None:
        result = int(values[0])
        for item in values:
            result = result and int(item)

        return result

    def nor_gate(self, values: list) -> None:
        result = not self.or_gate(values)

        if result == False:
            return '0'

        elif result == True:
            return '1'

    def nand_gate(self, values: list) -> None:
        result = not self.and_gate(values)

        if result == False:
            return '0'

        elif result == True:
            return '1'

    def xor_gate(self, values: list) -> None:
        result = ''
        for i in range(len(values) - 1):
            if values[i] != values[i+1]:
                result = '1'

            else:
                result = '0'

        return result
