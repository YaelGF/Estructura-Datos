from nodo import Nodo

class ListasSimples():

  def __init__(self):
    self.cabeza = None
    self.cola = None

  def vacia(self):
    return self.cabeza == None

  def agregar_inicio(self, dato):
    if self.vacia == True:
      self.cabeza = self.cola = Nodo(dato)
    else:
      aux = Nodo(dato)
      aux.siguiente = self.cabeza
      self.cabeza = aux

  def agregar_ultimo(self,dato):
    if self.vacia() == True :
      self.cabeza = self.cola = Nodo(dato)
    else:
      aux = self.cola
      self.cola = aux.siguiente = Nodo(dato)

  def eliminar_inicio(self):
    self.cabeza = self.cabeza.siguiente

  def eliminar_ultimo(self):
    aux = self.cabeza
    while aux.siguiente != self.cola:
      aux = aux.siguiente
    aux.siguiente = None
    self.cola = aux

  def buscar(self,dato):
    aux = self.cabeza
    while aux != None:
      if aux.dato == dato:
        return aux.dato
      aux = aux.siguiente
    return None

  def listar(self):
    aux = self.cabeza
    while aux != None:
      print(aux.dato)
      aux = aux.siguiente
  
  