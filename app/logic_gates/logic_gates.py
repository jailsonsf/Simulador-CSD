from app.logic_gates.gates import Gates

gates = {
    1: 'not',
    2: 'or',
    3: 'and',
    4: 'nor',
    5: 'nand',
    6: 'xor'
}


class LogicGates:
    def __init__(self) -> None:
        self.get_option()
        self.get_value()
        self.result()

    def show_gates(self) -> None:
        for key in gates:
            print(f'[{key}] - {gates[key]}')

    def get_option(self) -> None:
        print('Selecione a porta:')
        self.show_gates()

        option = int(input('>>> '))
        if option not in gates.keys():
            print('Opção inválida!')

        else:
            self.option = gates[option]

    def get_value(self) -> None:
        print(f'Digite o valor de entrada:')
        self.value = input('>>> ')

    def result(self) -> None:
        gate = Gates()

        if self.option == 'not':
            print(f'Resultado: {gate.not_gate(int(self.value))}')

        elif self.option == 'or':
            print(f'Resultado: {gate.or_gate(self.value)}')

        elif self.option == 'and':
            print(f'Resultado: {gate.and_gate(self.value)}')

        elif self.option == 'nor':
            print(f'Resultado: {gate.nor_gate(self.value)}')

        elif self.option == 'nand':
            print(f'Resultado: {gate.nand_gate(self.value)}')

        elif self.option == 'xor':
            print(f'Resultado: {gate.xor_gate(self.value)}')
