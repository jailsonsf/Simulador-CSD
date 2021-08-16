from time import sleep
from app.utils import clear

from app.unit_converter.unit_converter import UnitConverter
from app.base_converter.base_converter import Base_converter
from app.binary_sum.binary_sum import BinarySum
from app.logic_gates.logic_gates import LogicGates
from app.boolean_algebra.boolean_algebra import BooleanAlgebra


class App:
    def __init__(self) -> None:
        clear()
        menu = f'Digite [0] para Sair\nDigite [1] para converter unidades\nDigite [2] para converter bases\nDigite [3] para realizar soma binária\nDigite [4] para realizar operações de portas lógicas\nDigite [5] para analisar expressão da álgebra booleana'
        while True:
            print('='*40)
            print(menu)
            option = int(input('>>> '))

            if option == 0:
                print('Saindo...')
                sleep(1)
                clear()
                break
            elif option == 1:
                print(f'Opção [{option}]: Conversão de unidades de medida')
                UnitConverter()

                sleep(1)

            elif option == 2:
                print(f'Opção [{option}]: Conversão de bases numéricas')
                Base_converter()
                sleep(1)

            elif option == 3:
                print(f'Opção [{option}]: Soma binária')
                BinarySum()
                sleep(1)

            elif option == 4:
                print(f'Opção [{option}]: Operações com portas lógicas')
                LogicGates()
                sleep(1)

            elif option == 5:
                print(
                    f'Opção [{option}]: Analisar expressões da álgebra booleana')
                BooleanAlgebra()
                sleep(1)

            else:
                print(f'Opção inexistente!')
                sleep(1)
