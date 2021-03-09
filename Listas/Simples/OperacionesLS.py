from simples import ListasSimples

lista = ListasSimples()

lista.agregar_ultimo(5)
lista.agregar_ultimo(4)
lista.agregar_ultimo(3)

lista.agregar_inicio(6)
lista.agregar_inicio(7)

lista.listar()

print("*******")


search = lista.buscar(5)
if search != None:
  print("El dato ", search, " Si esta en la lista")
else:
  print("El dato No esta en la lista :C")

lista.eliminar_inicio()

lista.eliminar_ultimo()

print("*******")

lista.listar()