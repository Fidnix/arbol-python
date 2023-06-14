# Arbol Binario de Busqueda

Es una estructura de datos que permite realizar búsquedas más rápidas sobre sus elementos de lo que sería en una lista. En este pequeño repositorio realice el arbol binario con las siguientes funciones:

* **insertar**: Permite ingresar una lista desglosada de elementos para que se unan al árbol
* **insertar_ordenados**: Ordena una lista para insertarlos divididamnete en el árbol
* **\_\_str\_\_**: Permite convertir los datos del árbol en un str que contiene a todos los datos en una hilera. Se forman en preorden, postorden y en orden
* **obtener_nivel**: Obtiene el nivel del árbol
* **mayor**: Obtiene el mayor elemento del arbol
* **menor**: Obtiene el menor elemento del arbol
* **contar_nodos**: Devuelve el número de nodos en el árbol
* **sumar_nodos**: Devuelve la suma de todos los elementos del árbol
* **obtener_nodos_ordenados**: Devuelve una cola con todos los elementos recorridos por amplitud. Cabe mencionar que la cola contiene los nodos como si fueran de un arbol completo, y los nodos faltantes serán reemplazados por None
* **grafica**: Devuelve un str que asimila una grafica en forma de piramide del arbol

## Renderizado

A parte existe una clase que permite graficar al arbol con la ayuda de la librería tkinter. Simplemente debe crear una instancia y llamar al siguiente método:

```py
render = Render()
render.mostrar_arbol(arbol)
```

# Instalacion

Para poder usar el repositorio primero debe clonarlo, después debe crear un ambiente virtual:

```bash
python -m venv nombre_ambiente
```

Luego debe activarlo:

```bash
./nombre_ambiente/Scripts/activate
```

Y luego instalar lo requerido en el archivo requirements.txt:

```bash
pip install -r requirements.txt
```

A partir de ahí, puede ejecutar el programa
