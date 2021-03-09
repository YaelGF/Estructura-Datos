#https://pythondiario.com/2018/07/linked-list-listas-enlazadas.html
class Nodo:
  def __init__(self, nombre= None, sig = None):
    self.nombre = nombre
    self.sig = sig

  def __str__(self):
    return "%s" %(self.nombre)

class lSimples:
  def __init__(self):
    self.cabeza = None
    self.cola = None
  
  def agregar(self, elemento):
    if self.cabeza == None:
      self.cabeza = elemento
    if self.cola != None:
      self.cola.sig = elemento

    self.cola = elemento

  def listar(self):
    aux = self.cabeza
    while aux != None:
      print(aux)
      aux = aux.sig

  def buscar(self,nombre):
    aux = self.cabeza
    while aux != None:
      if aux.nombre == nombre:
        return aux
      aux = aux.sig
    return None

if __name__ == "__main__":
  ls = lSimples()

  while(True):
    print("----Menu----")
    print("1. Agregar")
    print("2. Listar")
    print("3. Buscar")
    num = input("Ingresar la opcion: ")
    if num == "1":
      nombre = input("Ingrese Nombre: ")
      nod = Nodo(nombre)
      ls.agregar(nod)
    elif num == "2":
      ls.listar()
    elif num == "3":
      nombre = input("Ingrese elnombre: ")
      result = ls.buscar(nombre)
      if result is not None:
        print (result)
      else:
        print("Registro no encontrado")