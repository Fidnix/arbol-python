from arbol.nodo import Nodo
from arbol.func import particion_lineal as pl, num_digitos
from arbol.colas import *

class Arbol:
    _raiz: Nodo

    def __init__(self, *elems) -> None:
        self._raiz = None
        if(len(elems) == 0):
            return
        self.insertar(*elems)
    def es_arbol_vacio(self) -> bool:
        return self._raiz == None
    
    def insertar(self, *elems: int)-> None:
        if(self._raiz == None):
            self._raiz = Nodo(None, elems[0])
            elem = elems[1:]
        if(len(elems)==0):
            return
        for elem in elems:
            self.insertar_uno(self._raiz, elem)
    def insertar_ordenados(self, *elems: int) -> None:
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
        # print(self._raiz._elem)
        self.insertar_recursivamente(self._raiz, elems)
    def insertar_recursivamente(self, N: Nodo = None, elems: list = []) -> None:
        if(len(elems) ==0):
            return
        
        if(len(elems) == 1):
            self.insertar_uno(N, elems[0])
            return
        l1, l2 = pl(N._elem, elems)

        void_ant: bool = False
        if(N._ant == None):
            p = N
            while(len(l1)!=0):
                p._ant = Nodo(None, l1.pop(), None)
                p = p._ant
            void_ant = True

        if(N._sig == None):
            p = N
            l2 = l2[::-1]
            while(len(l2)!=0):
                p._sig = Nodo(None, l2.pop(), None)
                p = p._sig
            return

        if(void_ant):
            return

        self.insertar_recursivamente(N._ant, l1)
        self.insertar_recursivamente(N._sig, l2)
        
        # return Nodo(N._ant, N._elem, N._sig)
    
    def insertar_uno(self, N: Nodo, elem: int) -> None:
        if(N == None):
            return
        aux = None
        p = N
        while(p !=None):
            aux = p
            if(p._elem < elem):
                p = p._sig
            elif (p._elem > elem):
                p = p._ant
            else:
                return
        if(aux._elem < elem):
            aux._sig = Nodo(None, elem, None)
        else:
            aux._ant = Nodo(None, elem, None)
        return

    def __str__(self, recorrido: str = 'en') -> str:
        if(self._raiz == None):
            return 'Arbol Vacio'

        if(recorrido == 'en'):
            return self.en_orden(self._raiz)[1:-1]
        elif(recorrido == 'post'):
            return self.post_orden(self._raiz)[1:-1]
        elif(recorrido == 'pre'):
            return self.pre_orden(self._raiz)[1:-1]
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
    def obtener_nodos_ordenados(self) -> Cola:
        if(self._raiz == None):
            return
        cola_final: Cola = Cola()
        N: NodoC = None

        max_n: int = self.obtener_nivel()
        arr_nodos: list = []
        
        for i in range(max_n):
            for _ in range(2**i):
                arr_nodos.append(None)

        arr_aux: list = [self._raiz]
        for i in range(len(arr_nodos)):
            N = arr_aux[0]
            arr_aux = arr_aux[1:]
            arr_nodos[i] = N

            if( N == None):
                arr_aux.append(None)
                arr_aux.append(None)
                continue
            if(N._ant != None):
                arr_aux.append(N._ant)
            else:
                arr_aux.append(None)
            if(N._sig != None):
                arr_aux.append(N._sig)
            else:
                arr_aux.append(None)

        for i in range(len(arr_nodos)):
            if(arr_nodos[i] != None):
                cola_final.encolar(arr_nodos[i]._elem)
            else:
                cola_final.encolar('None')
        return cola_final
    
    def grafica(self, C: Cola = None, mayor_elem: int = None) -> str:
        # Restriccion por arbol vacio
        if(self._raiz == None):
            return ''
        
        if(C == None):
            C = self.obtener_nodos_ordenados()

        if(mayor_elem == None):
            mayor_elem = self.mayor()
        
        out: str = '' # Salida principal

        # Datos de nivel
        max_n = self.obtener_nivel()
        current_n: int = 0
        potencia: int = 1

        # Datos de formato
        tam_lado: int = 3
        tam_nodo: int = max(4, num_digitos(mayor_elem)) + 2

        # Funciones de formato
        margen: callable = lambda n: (int(2**(max_n - n)) - 1)*(tam_nodo + tam_lado)
        espacio_entre_nodos: callable = lambda n: int((2**(max_n - n+1))*(tam_lado + tam_nodo) - tam_nodo)
        dibujo_nodo: callable = lambda nodo: f'({nodo:>{tam_nodo-2}})' if nodo != 'None' else f'({" ":>{tam_nodo-2}})'

        long: int = C._size
        elem: int = None
        for i in range(1,long+1):
            elem = C.desencolar()
            if(i == potencia):
                current_n += 1
                out += f'\n\n\n\n{" "*margen(current_n)}{dibujo_nodo(elem)}'
                # print(f'margen: {current_n}, {margen(current_n)}')
                potencia *= 2
            else:
                # print(f'margen: {current_n}, {espacio_entre_nodos(current_n)}')
                out += f'{" "*(espacio_entre_nodos(current_n))}{dibujo_nodo(elem)}'
        return out