from arbol import *
from colorama import Fore, Style
def test():
    arb1 = Arbol()
    print(Fore.YELLOW + 'Primera prueba de arbol: Insercion de varios elementos' + Style.RESET_ALL)
    arb1.insertar(2,3,4,7)
    print(f'Arbol al cual se añadio los elementos [2,3,4,7]: {arb1}')
    arb1.insertar(8, 9, 10)
    print(f'Arbol al cual se añadio los elementos [8,9,10]: {arb1}')
    arb1.insertar(5)
    print(f'Arbol al cual se añadio los elementos [5]: {arb1}')
    arb1.insertar(1,6)
    print(f'Arbol al cual se añadio los elementos [1,6]: {arb1}')
    print(Fore.YELLOW + 'Segunda prueba: Funciones basicas del arbol' + Style.RESET_ALL)
    print(f'Obtencion del nivel del arbol: {arb1.obtener_nivel()}')
    print(f'Obtencion del menor elemento del arbol: {arb1.menor()}')
    print(f'Obtencion del mayor elemento del arbol: {arb1.mayor()}')
    print(f'Obtencion del numero de nodos del arbol: {arb1.contar_nodos()}')
    print(f'Obtencion de la suma de todos los elementos del arbol: {arb1.sumar_nodos()}')

def test2():
    
    arb = Arbol(8)
    print(Fore.YELLOW + 'Tercera prueba de arbol: Grafica de un arbol' + Style.RESET_ALL)
    arb.insertar(12)
    arb.insertar(4)
    arb.insertar(1)
    arb.insertar(14)
    arb.insertar(7)
    arb.insertar(15)
    print(f'Arbol impreso en orden: {arb}')

    cola_nodos: Cola = arb.obtener_nodos_ordenados()
    print(f'Cola de nodos obtenida para la grafica: {cola_nodos}')
    # print(cola_nodos._size)
    # print(f'{arb._raiz._ant._elem} - {arb._raiz._sig._elem}')
    print('Grafica del arbol:')
    print(arb.grafica(C=cola_nodos))
    # print(arb.obtener_nodos_ordenados(arb._raiz, arb.obtener_nivel() , 1))