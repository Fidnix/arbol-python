from arbol.func import *
from colorama import Fore, Style

def test():
    # Pruebas de particion lineal
    elem: int = 7
    inputs: list[list[int]] = [
        [1,6,7],
        [6,7,8,9],
        [1,2,3,4,7,8,9],
        [1,7,8],

        [1,6],
        [6,8,9],
        [1,2,3,4,8,9],
        [1,2,3,4,5,6,8,9],
        [1,8],
        [8,9,10,11],
    ]

    outputs: list[tuple[int]] = [
        ([1,6], []),
        ([6], [8,9]),
        ([1,2,3,4], [8,9]),
        ([1], [8]),
        ([1,6], []),
        ([6], [8,9]),
        ([1,2,3,4], [8,9]),
        ([1,2,3,4,5,6], [8,9]),
        ([1], [8]),
        ([], [8,9,10,11]),
    ]

    for input, output in zip(inputs, outputs):
        x = particion_lineal(elem, input)
        assert x == output, f'No funciona: Salida generada: {x}\nSalida esperada: {output}'
    
    assert ([2], [6]) == particion_lineal(4, [2,6]), f'No funciona: Salida generada: {particion_lineal(4, [2,6])}\nSalida esperada: {([2], [6])}'

    inputs2: list = [
        20,
        100,
        1,
        1078,
        45403
    ]

    outputs2: list = [
        2,
        3,
        1,
        4,
        5
    ]

    for inp, outp in zip(inputs2, outputs2):
        sol: int = num_digitos(inp)
        assert sol == outp, f'Se esperaba que el numero de digitos de {inp} sea: outp. En su lugar se obtuvo {sol}'
    print(Fore.GREEN + 'Pruebas de func realizadas correctamente :D' + Style.RESET_ALL)