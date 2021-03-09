from dobleEnla import ListaDoble
from os import system

system("clear")

ls = ListaDoble()

ls.agregar_final(9)
ls.agregar_final(8)
ls.agregar_final(7)

ls.agregar_inicio(1)
ls.agregar_inicio(2)

ls.recorrer_inicio()

print("=========")

ls.recorrer_fin()

print("==========")

ls.eliminar_final()

ls.eliminar_inicio()

ls.recorrer_inicio()

print("=========")

ls.recorrer_fin()