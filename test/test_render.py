from arbol import *
from colorama import Fore, Style

def test():
    arbol: Arbol = Arbol()
    numeros: list = [16] + list(range(8,28,16)) + list(range(4,29, 8)) + list(range(2, 31,4)) + list(range(1,32))
    arbol.insertar(*numeros)

    render = Render()
    render.mostrar_arbol(arbol)
    print(Fore.GREEN + 'Renderizado del arbol realizado con exito' + Style.RESET_ALL)