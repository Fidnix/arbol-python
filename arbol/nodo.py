class Nodo:
    _elem: int
    _sig: 'Nodo'
    _ant: 'Nodo'

    def __init__(self, ant: 'Nodo' = None, elem: int = 0, sig: 'Nodo' = None) -> None:
        self._elem = elem
        self._sig = sig
        self._ant = ant

    def __str__(self, N: 'Nodo' = None) -> str:
        if(N == None):
            return ''
        str1: str = self.__str__(N._ant)
        str2: str = self.__str__(N._sig)

        return f'{str1} {N._elem} {str2}'