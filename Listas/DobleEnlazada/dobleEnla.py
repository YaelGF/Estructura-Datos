from nodo import Nodo
class ListaDoble():
  def __init__(self):
    self.cabeza = None
    self.cola = None
    self.size = 0
  
  def vacia(self):
    return self.cabeza == None
  
  def agregar_final(self, dato):
    if self.vacia():
      self.cabeza = self.cola = Nodo(dato)
    else:
      aux = self.cola
      self.cola = aux.siguiente = Nodo(dato)
      self.cola.anterior = aux
    self.size += 1
  
  def agregar_inicio(self,dato):
    if self.vacia():
      self.cabeza = self.cola = Nodo(dato)
    else:
      aux = Nodo(dato)
      aux.siguiente = self.cabeza
      self.cabeza.anterior = aux
      self.cabeza = aux
    self.size += 1

  def recorrer_inicio(self):
    aux = self.cabeza
    while aux:
      print(aux.dato)
      aux = aux.siguiente

  def recorrer_fin(self):
    aux = self.cola
    while aux:
      print(aux.dato)
      aux = aux.anterior

  def Size(self):
    return self.size

  def eliminar_inicio(self):
    if self.vacia():
      print("Esta Vacia")
    elif self.cabeza.siguiente == None:
      self.cabeza = self.cola = None
      self.size = 0
    else:
      self.cabeza = self.cabeza.siguiente
      self.cabeza.anterior = None
      self.size -= 1

  def eliminar_final(self):
    if self.vacia():
      print("Esta Vacia")
    elif self.cabeza.siguiente == None:
      self.cabeza = self.cola = None
      self.size = 0
    else:
      self.cola = self.cola.anterior
      self.cola.siguiente = None
      self.size -= 1