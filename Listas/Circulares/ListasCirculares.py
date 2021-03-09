from os import system
class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None

class ListaCircular():

  def __init__(self):
    self.primero = None
    self.ultimo = None
  
  def vacia(self):
    return self.primero == None
  
  def agregar_final(self, dato):
    if self.vacia():
      self.primero = self.ultimo = Nodo(dato)
      self.ultimo.siguiente = self.primero
    else:
      aux = self.ultimo
      self.ultimo = aux.siguiente = Nodo(dato)
      self.ultimo.siguiente = self.primero
  
  def agregar_inicio(self,dato):
    if self.vacia():
      self.primero = self.ultimo = Nodo(dato)
      self.ultimo.siguiente = self.primero
    else:
      aux = Nodo(dato)
      aux.siguiente = self.primero
      self.primero = aux
      self.ultimo.siguiente = self.primero

  def recorrer(self):
    aux = self.primero
    #ciclo infinito
    #while aux:
    while aux.siguiente != self.primero:
      print(aux.dato)
      aux = aux.siguiente
    print(aux.dato)

if __name__ == "__main__":
  system("clear")
  lc = ListaCircular()

  lc.agregar_final(3)
  lc.agregar_final(4)
  lc.agregar_final(5)
  lc.agregar_final(6)
  lc.agregar_inicio(2)

  lc.recorrer()