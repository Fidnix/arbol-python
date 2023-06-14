# No funciono, se supone que debia dividir listas mediante el enfoque: divide and conquer
def particion_binaria(elem: int = None, elems: list = []) -> tuple:
        if(elem==None or len(elems) == 0):
            return ()
        if(len(elems) == 1):
            if(elem == elems[0]):
                return ([], [])
            elif (elem > elems[0]):
                return (elems, [])
            else:
                return ([], elems)
        
        inicio: int = 0
        mitad: int = len(elems)//2
        final: int = len(elems)
        while(elems[mitad] != elem):
            print(f'({inicio=}, {mitad=}, {final=}) - {elems[mitad]} - {elem}')
            # if(inicio >= final):
            #     break

            if(elems[mitad] > elem):
                final = mitad-1
            else:
                inicio = mitad+1
            mitad = (final+inicio)//2

            if(inicio >= final):
                break
            # if(final < inicio):
            #     break
            # mitad = (final+inicio)//2
            # if(elems[mitad]>elem):
            #     final = mitad + 1
            # else:
            #     inicio = mitad
        print(f'({inicio=}, {mitad=}, {final=}) - {elem}')
        if(len(elems)<= mitad):
            return (elems[:mitad], elems[mitad:])
        if(elems[mitad]==elem):
            return (elems[:mitad], elems[mitad+1:])
        return (elems[:mitad], elems[mitad:])

def particion_lineal(elem: int = None, elems: list = []) -> tuple:
    pos: int = 0
    for item in elems:
        if(item == elem):
            return ( elems[:pos], elems[pos+1:] )
        if(elem < item):
            return ( elems[:pos], elems[pos:] )
        pos += 1
    return ( elems, [] )

def num_digitos(num: int = 9):
    if(num < 10):
        return 1
    return 1 + num_digitos(num/10)