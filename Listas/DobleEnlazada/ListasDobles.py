from os import system
class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None
    self.anterior = None
  
class ListaDoble():
  def __init__(self):
    self.primero = None
    self.ultimo = None
    self.size = 0
  
  def vacia(self):
    return self.primero == None
  
  def agregar_final(self, dato):
    if self.vacia():
      self.primero = self.ultimo = Nodo(dato)
    else:
      aux = self.ultimo
      self.ultimo = aux.siguiente = Nodo(dato)
      self.ultimo.anterior = aux
    self.size += 1
  
  def agregar_inicio(self,dato):
    if self.vacia():
      self.primero = self.ultimo = Nodo(dato)
    else:
      aux = Nodo(dato)
      aux.siguiente = self.primero
      self.primero.anterior = aux
      self.primero = aux
    self.size += 1

  def recorrer_inicio(self):
    aux = self.primero
    while aux:
      print(aux.dato)
      aux = aux.siguiente

  def recorrer_fin(self):
    aux = self.ultimo
    while aux:
      print(aux.dato)
      aux = aux.anterior


if __name__ == "__main__":
  system("clear")
  ld =  ListaDoble()

  ld.agregar_inicio(4)
  ld.agregar_inicio(3)
  ld.agregar_inicio(2)
  ld.agregar_inicio(1)
  ld.agregar_final(5)

  ld.recorrer_inicio()
  print("*****************")
  ld.recorrer_fin()