from time import sleep
from app.utils import clear

from app.unit_converter.unit_converter import UnitConverter
from app.base_converter.base_converter import Base_converter


class App:
    def __init__(self) -> None:
        clear()
        while True:
            print('='*40)
            print(f'Digite [0] para Sair')
            print(f'Digite [1] para converter unidades')
            print(f'Digite [2] para converter bases')
            print(f'Digite [3] para realizar soma binária')
            print(f'Digite [4] para realizar operações de portas lógicas')
            print(f'Digite [5] para analisar expressão da álgebra relacional')
            option = int(input('>> '))

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
                sleep(1)

            elif option == 4:
                print(f'Opção [{option}]: Operações com portas lógicas')
                sleep(1)

            elif option == 5:
                print(
                    f'Opção [{option}]: Analisar expressões da álgebra relacional')
                sleep(1)

            else:
                print(f'Opção inexistente!')
                sleep(1)
