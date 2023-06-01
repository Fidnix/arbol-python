from typing import Union

class NodoC:
    _sig: 'NodoC'
    _elem: int

    def __init__(self, elem: Union[int, str] = None):
        if(elem == None):
            return None
        self._sig = None
        self._elem = elem