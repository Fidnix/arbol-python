from arbol import *
from colorama import Fore, Style

def test():
    C: Cola = Cola()

    assert C._frente == None, 'Se esperaba que el frente de la cola fuera diferente de None' 
    assert C.__str__(sep = ' ') == 'Cola vacia', f'No coinciden las salidas:\nSalida esperada: ""\nSalida generada: {C.__str__(sep = " ")}'
    
    C.encolar(4)
    C.encolar(5)

    assert C._frente != None, 'Se esperaba que el frente de la cola fuera diferente de None' 
    assert C._frente._elem == 4, 'El elemento esperado era 4 (int)' 
    assert C.__str__(sep = ' ') == '5 4', f'No coinciden las salidas:\nSalida esperada: "5 4"\nSalida generada: {C.__str__(sep = " ")}'
    
    x = C.desencolar()
    assert x == 4, 'Se esperaba que el elemento a eliminar fuera 4 y su salida fuera 4' 
    assert C.__str__(sep = ' ') == '5', f'No coinciden las salidas:\nSalida esperada: "5"\nSalida generada: {C.__str__(sep = " ")}'
    
    C.encolar()
    # assert C._frente._elem == None, 'Se esperaba que el elemento agregado fuera None' 
    assert C.__str__(sep = ' ') == '5', f'No coinciden las salidas:\nSalida esperada: "5"\nSalida generada: {C.__str__(sep = " ")}'
    # print(C)
    C.desencolar()
    C.desencolar()
    C.desencolar()
    assert C._frente == None, 'El frente debe ser None al eliminar todos los elementos' 
    x = C.desencolar()
    assert x == None, 'Si se trata de eliminar un elemento de una cola vacia, la salida debe ser None'
    # print(C)

    C.encolar(1)
    C.encolar(2)
    C.encolar(3)

    # P2: Cola = Cola(4)
    # P2.encolar(5)
    # P2.encolar(6)
    # P2.encolar(7)
    # P2.encolar(8)

    # C.fusionar(P2)

    long: int = C._size
    arr = [C.desencolar() for _ in range(long) ]

    esperado = list(range(1,4))
    for index, item in zip( range(3), esperado):
        if(arr[index] != item):
            raise AssertionError(f'Las salidas ni concuerdan: Salida esperada: {esperado}\nSalida generada: {arr}')
    print(Fore.GREEN + f'Pruebas de las pilas realizadas correctamente :D' + Style.RESET_ALL)