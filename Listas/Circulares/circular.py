from nodo import Nodo
class ListaCircular():

  def __init__(self):
    self.cabeza = None
    self.cola = None
  
  def vacia(self):
    return self.cabeza == None
  
  def agregar_final(self, dato):
    if self.vacia():
      self.cabeza = self.cola = Nodo(dato)
      self.cola.siguiente = self.cabeza
    else:
      aux = self.cola
      self.cola = aux.siguiente = Nodo(dato)
      self.cola.siguiente = self.cabeza
  
  def agregar_inicio(self,dato):
    if self.vacia():
      self.cabeza = self.cola = Nodo(dato)
      self.cola.siguiente = self.cabeza
    else:
      aux = Nodo(dato)
      aux.siguiente = self.cabeza
      self.cabeza = aux
      self.cola.siguiente = self.cabeza

  def recorrer(self):
    aux = self.cabeza
    #ciclo infinito
    #while aux:
    while aux.siguiente:
      print(aux.dato)
      aux = aux.siguiente
      if aux == self.cabeza:
        break
  
  def eliminar_inicio(self):
    if self.vacia():
      print("lista Vacia")
    elif self.cabeza == self.cola:
      self.cabeza = self.cola = None
    else:
      self.cabeza = self.cabeza.siguiente
      self.cola.siguiente = self.cabeza

  def eliminar_final(self):
    if self.vacia():
      print("lista Vacia")
    elif self.cabeza == self.cola:
      self.cabeza = self.cola = None
    else:
      aux = self.cabeza
      while aux.siguiente != self.cola:
        aux = aux.siguiente
      aux.siguiente = self.cabeza
      self.cola = aux