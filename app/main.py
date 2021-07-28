from time import sleep
from utils import clear

while True:
    clear()

    print(f'Digite [0] para Sair')
    print(f'Digite [1] para converter unidades')
    print(f'Digite [2] para converter bases')
    print(f'Digite [3] para realizar soma binária')
    print(f'Digite [4] para realizar operações de portas lógicas')
    print(f'Digite [5] para analisar expressão da álgebra relacional')
    option = int(input('Selecione uma opção: '))

    if option == 0:
        print('Saindo...')
        break
    elif option == 1:
        print(f'Opção {option}: Conversão de unidades de medida')
        sleep(1)

    elif option == 2:
        print(f'Opção {option}: Conversão de bases numéricas')
        sleep(1)

    elif option == 3:
        print(f'Opção {option}: Soma binária')
        sleep(1)

    elif option == 4:
        print(f'Opção {option}: Operações com portas lógicas')
        sleep(1)

    elif option == 5:
        print(f'Opção {option}: Analisar expressões da álgebra relacional')
        sleep(1)

    else:
        print(f'Opção inexistente!')
        sleep(1)