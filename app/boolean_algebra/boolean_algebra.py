class BooleanAlgebra:
    def __init__(self) -> None:
        self.get_expression()
        self.validate_expression(list(self.expression))

    def get_expression(self) -> None:
        print(f'Digite a expressão boolean:')
        self.expression = list(input('>>> ').lower().split())

    def validate_expression(self, expression: list) -> None:
        if expression[0] == 'not':
            if expression[1].isalpha():
                print('Expressão Válida')

            else:
                print('Expressão Inválida')

        else:
            if expression[0].isalpha():
                if (expression[1] == 'or' or expression[1] == 'and' or expression[1] == 'nor' or expression[1] == 'nand' or expression[1] == 'xor') and expression[2].isalpha():
                    print('Expressão Válida')

                else:
                    print('Expressão Inválida')
