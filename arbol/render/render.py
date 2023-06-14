from ..abb import Arbol
from ..nodo import Nodo
from tkinter import Tk, Canvas

class Render():

    def __init__(self):
        self._ancho: int = 1200
        self._alto: int = 800
        self._arista: int = 30
        self._radio_nodo: int = 10
        self._margen: int = 20
        self._sep_nivel: int = 80
        self._ventana, self._lienzo = self.crear_lienzo('Arbol binario de busqueda')

    def crear_lienzo(self, titulo: str = "Lienzo"):
        window = Tk()
        window.geometry(f"{self._ancho}x{self._alto}")
        window.title(titulo)
        lienzo = Canvas(window, width=self._ancho, height=self._alto, bg='#000')
        lienzo.place(x=0, y=0)
        return window, lienzo
    
    def arista(self, nivel: int = 1):
        if(nivel == 1):
            return 0
        return (self._arista + self._radio_nodo)* 2**(nivel-2) - self._radio_nodo

    def circulo_centrado(self, x = 10, y = 10, radio = 10, relleno: str = '#fff'):
        self._lienzo.create_oval(
            x-radio,
            y-radio,
            x+ 2*radio,
            y+ 2*radio,
            fill = relleno,
            outline = relleno
        )

    def mostrar_nodo(self, val: int = 0, x: int = 10, y: int = 10, radio: int = 10):
        self.circulo_centrado(x, y, radio)
        self._lienzo.create_text(
            x+radio/2,
            y+radio/2,
            text = str(val),
            fill = '#000',
            font=('Helvetica 10 bold')
        )

    def mostrar_nodos_recursivamente(
        self,
        nodo: Nodo = None,
        nivel: int = 0,
        x: int = 0,
        y: int = 0,
        x_padre: int = 0,
        y_padre: int = 0,
    ):
        if(nodo == None):
            return
        self._lienzo.create_line(x_padre, y_padre, x, y, width = 3.0, fill='#fff')
        self.mostrar_nodos_recursivamente(
            nodo._ant,
            nivel - 1,
            x = x - self.arista(nivel),
            y = y + self._sep_nivel,
            x_padre = x,
            y_padre = y)
        self.mostrar_nodos_recursivamente(
            nodo._sig,
            nivel - 1,
            x = x + self.arista(nivel),
            y = y + self._sep_nivel,
            x_padre = x,
            y_padre = y)
        self.mostrar_nodo(nodo._elem, x, y, self._radio_nodo)

    def mostrar_arbol(self, arbol: Arbol = None) -> None:
        if(arbol == None):
            return

        nivel: int = arbol.obtener_nivel()
        x_raiz = self._ancho/2
        y_raiz = (self._margen+self._radio_nodo)


        self.mostrar_nodos_recursivamente(
            arbol._raiz._ant,
            nivel - 1,
            x = x_raiz - self.arista(nivel),
            y = y_raiz + self._sep_nivel,
            x_padre = self._ancho/2,
            y_padre = (self._margen+self._radio_nodo),
        )
        self.mostrar_nodos_recursivamente(
            arbol._raiz._sig,
            nivel - 1,
            x = x_raiz + self.arista(nivel),
            y = y_raiz + self._sep_nivel,
            x_padre = self._ancho/2,
            y_padre = (self._margen+self._radio_nodo),
        )
        self.mostrar_nodo(
            arbol._raiz._elem,
            x = x_raiz,
            y = y_raiz,
            radio = self._radio_nodo
        )
        self._ventana.mainloop()