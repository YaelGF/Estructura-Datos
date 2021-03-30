from node import Node

class BinaryTree:
  def __init__(self):
    self.root = None

  def empty(self):
    if self.root == None:
      return True
    else:
      return False

  def add(self, value):
    if self.empty():
      self.root = Node(value=value)
    else:
      nodo = self.__get_place(value)
      if value <= nodo.value:
        nodo.left = Node(value=value, parent=nodo, is_left=True)
      else:
        nodo.right = Node(value= value,parent=nodo, is_right=True)


  def __get_place(self, value):
    aux = self.root
    while aux:
      temp = aux
      if value <= aux.value:
        aux = aux.left
      else:
        aux = aux.right
    return temp

  def showorden(self, node):
    if node:
      self.showorden(node.left)
      print(node.value)
      self.showorden(node.right)

  def showpre_orden(self, node):
    if node:
      print(node.value)
      self.showpre_orden(node.left)
      self.showpre_orden(node.right)

  def showpos_orden(self, node):
    if node:
      self.showpos_orden(node.left)
      self.showpos_orden(node.right)
      print(node.value)

  def search(self, node, value):
    if node == None:
      return None
    else:
      if node.value == value:
        return node
      elif value <= node.value:
        return self.search(node.left, value)
      else:
        return self.search(node.right, value)

  def eliminar(self, node, value):
    if node == None:
      
    else:
      if node.value == value:
        return node
      elif value <= node.value:
        return self.search(node.left, value)
      else:
        return self.search(node.right, value)
    
