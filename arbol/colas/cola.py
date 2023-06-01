from typing import Union
from .nodoC import NodoC

class Cola:
    _size: int
    _frente: NodoC
    _final: NodoC

    def __init__(self, elem: Union[int, str] = None):
        if(elem == None):
            self._frente = None
            self._final = None
            self._size = 0
            return
        self._frente = NodoC(elem)
        self._final = self._frente
        self._size = 1

    def encolar(self, elem: Union[int, str] = None) -> None:
        if(elem == None):
            return
        if(self._frente == None):
            self._size = 1
            self._frente = NodoC(elem)
            self._final = self._frente
            return
        self._final._sig = NodoC(elem)
        self._final = self._final._sig
        self._size += 1

    def desencolar(self) -> list:
        if(self._frente == None):
            return None
        p = self._frente._elem
        self._frente = self._frente._sig
        self._size -= 1
        return p
    def __str__(self, sep: str = ' > ') -> str:
        if(self._frente == None):
            return 'Cola vacia'
        p = self._frente
        arr: list = []
        for _ in range(self._size):
            arr.append(p._elem)
            p = p._sig
        return f'{sep.join(str(e) for e in arr[::-1])}'
    
    # def fusionar(self, C: 'Cola') -> None:
    #     if(C._size == 0):
    #         return
    #     aux: int
    #     long: int = C._size
    #     for i in range(1, long):
    #         for _ in range(long - i):
    #             self.push(C.pop())

    #         aux = C.pop() # Guarda el ultimo elemento

    #         for _ in range(long - i):
    #             C.push(self.pop())
    #         self.push(aux)
    #     self.push(C.pop())