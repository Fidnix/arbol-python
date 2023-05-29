from arbol import *

if __name__ == '__main__':
    xd = Arbol()
    xd.insertar(2,3,4,7)
    print(xd)
    xd.insertar(8, 9, 10)
    print(xd)
    xd.insertar(5)
    print(xd)
    xd.insertar(1,6)
    print(xd)
    print(xd.obtener_nivel())
    print(xd.__str__('pre'))
    print(xd.menor())
    print(xd.mayor())
    print(xd.contar_nodos())
    print(xd.sumar_nodos())