from circular import ListaCircular
from os import system

system("clear")

ls = ListaCircular()

ls.agregar_final(9)
ls.agregar_final(8)
ls.agregar_final(7)

ls.agregar_inicio(2)
ls.agregar_inicio(1)

ls.recorrer()

print("*"*25)

ls.eliminar_final()
ls.eliminar_inicio()

ls.recorrer()

print("ultimo.siguiente: ", ls.cola.siguiente.dato)