from arbol.nodo import Nodo
from arbol.func import particion_lineal as pl

class Arbol:
    _raiz: Nodo

    def __init__(self, *elems) -> None:
        self._raiz = None
        if(len(elems) == 0):
            return
        self.insertar(elems)
    def es_arbol_vacio(self) -> bool:
        return self._raiz == None
    
    def insertar(self, *elems: int) -> None:
        if(len(elems) == 0):
            return
        elems = sorted(elems)
        if(self._raiz == None):
            self._raiz = Nodo(None, elems.pop())
            p = self._raiz
            while(len(elems) != 0):
                p._ant = Nodo(None, elems.pop(), None)
                p = p._ant
            return
        
        self._raiz = self.insertar_recursivamente(self._raiz, elems)
    def insertar_recursivamente(self, N: Nodo = None, elems: list = []) -> Nodo:
        if(len(elems) ==0):
            return N
        
        if(len(elems) == 1):
            return self.insertar_uno(N, elems[0])
        
        l1, l2 = pl(N._elem, elems)

        # print(f'{N.__str__(N)=}')
        # print(f'({l1=}, {l2=})')

        if(N._ant == None):
            p = N
            while(len(l1)!=0):
                p._ant = Nodo(None, l1.pop(), None)
                p = p._ant
            return N
        if(N._sig == None):
            p = N
            l2 = l2[::-1]
            while(len(l2)!=0):
                p._sig = Nodo(None, l2.pop(), None)
                p = p._sig
            return N


        N._ant = self.insertar_recursivamente(N._ant, l1)
        N._sig = self.insertar_recursivamente(N._sig, l2)
        
        return Nodo(N._ant, N._elem, N._sig)
    
    def insertar_uno(self, N: Nodo, elem: int) -> Nodo:
        if(N == None):
            return Nodo(None, elem, None)
        aux = None
        p = N
        while(p !=None):
            aux = p
            if(p._elem < elem):
                p = p._sig
            elif (p._elem > elem):
                p = p._ant
            else:
                return N
        if(aux._elem < elem):
            aux._sig = Nodo(None, elem, None)
        else:
            aux._ant = Nodo(None, elem, None)
        return N

    def __str__(self, recorrido: str = 'en') -> str:
        if(self._raiz == None):
            return 'Arbol Vacio'

        if(recorrido == 'en'):
            return self.en_orden(self._raiz)
        elif(recorrido == 'post'):
            return self.post_orden(self._raiz)
        elif(recorrido == 'pre'):
            return self.pre_orden(self._raiz)
        else:
            raise ValueError(f'No es valido el tipo de recorrido: {recorrido}. Solo puede usar: "pre", "post" o "en"')

    def pre_orden(self, N: Nodo = None) -> str:
        if(N == None):
            return ''
        str1: str = self.pre_orden(N._ant)
        str2: str = self.pre_orden(N._sig)

        return f'{N._elem} {str1} {str2}'
    
    def en_orden(self, N: Nodo = None) -> str:
        if(N == None):
            return ''
        str1: str = self.en_orden(N._ant)
        str2: str = self.en_orden(N._sig)

        return f'{str1} {N._elem} {str2}'
    
    def post_orden(self, N: Nodo = None) -> str:
        if(N == None):
            return ''
        str1: str = self.post_orden(N._ant)
        str2: str = self.post_orden(N._sig)

        return f'{str1} {str2} {N._elem}'


    def obtener_nivel(self) -> int:
        if(self._raiz == None):
            return 0
        return self.nivel_recursivo(self._raiz)
    def nivel_recursivo(self, N: Nodo = None) -> int:
        if(N == None):
            return 0
        nivel_ant = self.nivel_recursivo(N._ant)
        nivel_sig = self.nivel_recursivo(N._sig)

        if(nivel_sig > nivel_ant):
            return nivel_sig + 1
        else:
            return nivel_ant + 1

    def menor(self) -> int:
        if(self._raiz == None):
            return
        p = self._raiz
        while(p._ant != None):
            p = p._ant
        return p._elem

    def mayor(self) -> int:
        if(self._raiz == None):
            return
        p = self._raiz
        while(p._sig != None):
            p = p._sig
        return p._elem

    def contar_nodos(self) -> int:
        if(self._raiz == None):
            return 0
        return self.contar_recursivo(self._raiz)
    def contar_recursivo(self, N: Nodo = None) -> int:
        if(N == None):
            return 0

        val_ant = self.contar_recursivo(N._ant)
        val_sig = self.contar_recursivo(N._sig)

        return 1 + val_ant + val_sig

    def sumar_nodos(self) -> int:
        if(self._raiz == None):
            return 0
        return self.sumar_recursivo(self._raiz)
    def sumar_recursivo(self, N: Nodo = None) -> int:
        if(N == None):
            return 0

        val_ant = self.sumar_recursivo(N._ant)
        val_sig = self.sumar_recursivo(N._sig)

        return N._elem + val_ant + val_sig

    def grafica(self) -> str:
        if(self._raiz == None):
            return ''
        return self.grafica_recursiva(self._raiz, 1)
    def grafica_recursiva(self, N: Nodo = None, nivel: int = 0) -> str:
        pass