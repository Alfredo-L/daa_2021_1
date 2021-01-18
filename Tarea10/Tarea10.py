#Las capturas son representaciones gráficas de los arboles binarios para comparar los resultados
class NodoArbol:
    def __init__(self, value, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right

    def hojas(self, nod):
        if nod == None:
            return None
        else:
            self.hojas(nod.left)
            self.hojas(nod.right)
            if nod.left == None and nod.right == None:
                print(f"Nodo hoja es {nod.data}")

print("\n")
arbol1 = NodoArbol(1,NodoArbol(2,None,NodoArbol(4)),NodoArbol(3,NodoArbol(5),None))
print("Arbol 1:")
arbol1.hojas(arbol1)
print("\n")

arbol2 = NodoArbol("X",NodoArbol("Y",None,NodoArbol("Z",NodoArbol("M",None,NodoArbol("N",NodoArbol("A"),None)),None)),None)
print("Arbol 2:")
arbol2.hojas(arbol2)
print("\n")

arbol3 = NodoArbol(5,NodoArbol(17,NodoArbol(45,NodoArbol(38),NodoArbol(22)),NodoArbol(58,NodoArbol(7),NodoArbol(11))),NodoArbol(23,NodoArbol(79,NodoArbol(4),NodoArbol(8)),NodoArbol(93,NodoArbol(76),NodoArbol(98))))
print("Arbol 3:")
arbol3.hojas(arbol3)
print("\n")

arbol4 = NodoArbol("Seat",NodoArbol("Kia",NodoArbol("Mazda",NodoArbol("Chevrolet")),None),NodoArbol("Honda",None,NodoArbol("Nissan",None,NodoArbol("Ford"))))
print("Arbol 4:")
arbol4.hojas(arbol4)
print("\n")