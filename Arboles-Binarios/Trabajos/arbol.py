class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato
 
def insertar(raiz, nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None:
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                insertar(raiz.izquierda, nodo)

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.dato)
        inorden(raiz.derecha)

def preorden(raiz):
    if raiz is not None:
        print(raiz.dato)
        preorden(raiz.izquierda)
        preorden(raiz.derecha)

def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izquierda)
        postorden(raiz.derecha)
        print(raiz.dato)

def buscar_dato(raiz, dato):
    if raiz is None:
        return False
    elif raiz.dato == dato:
        return True
    elif dato < raiz.dato:
        return buscar_dato(raiz.izquierda, dato)
    else:
        return buscar_dato(raiz.derecha, dato)

def valorminimo(node):
    current = node
    while(current.izquierda is not None):
        current = current.izquierda
    return current
    
def eliminar(raiz,dato):
    if raiz is None:
        return raiz
    if dato < raiz.dato:
        raiz.izquierda = eliminar(raiz.izquierda, dato)
    elif(dato > raiz.dato):
        raiz.derecha = eliminar(raiz.derecha, dato)
    else:
        if raiz.izquierda is None:
            temp = raiz.derecha
            raiz = None
            return temp
        elif raiz.derecha is None:
            temp = raiz.izquierda
            raiz = None
            return temp
    temp = valorminimo(raiz.derecha)
    raiz.dato = temp.dato
    raiz.derecha  = eliminar(raiz.derecha, temp.dato)



if __name__ == "__main__":

    while True:
        print("\nMenu")
        print("1) Insertar raiz")
        print("2) Insertar dato")
        print("3) Buscar dato")
        print("4) Impresion Posorden")
        print("5) Impresion Inorden")
        print("6) Impresion Preorden")
        print("8) Salir")
        opcion = int(input("\nIngrese su opcion: "))   
        if opcion == 1:
            r = int(input("\nQue raiz quiere establecer?: "))
            raiz = Nodo(r)    
        elif opcion == 2:
            numero = int(input("Que numero desea insertar?: "))
            insertar(raiz,Nodo(numero))
            print("Numero insertado")
            
        elif opcion == 3:
            numero = int(input("Que numero desea buscar?: "))
            print("Existe el dato: ", buscar_dato(raiz,numero))
            
        elif opcion == 4:
            print("Posorden")
            postorden(raiz)
        elif opcion == 5:
            print("Inorden")
            inorden(raiz)
        elif opcion == 6:
            print("Preorden")
            preorden(raiz)
        elif opcion == 7:
            dato = int(input("Que hoja desea eliminar?: "))
            eliminar(raiz,dato)
            print("Hoja eliminada") 

        elif opcion == 8:
            exit()
        else:
            print("Escoja una opcion valida")