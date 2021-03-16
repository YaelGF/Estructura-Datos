from pila import Pila
from os import system

system("clear")

pila = Pila()

pila.push(23)
pila.push(51)
pila.push(45)
pila.push(90)
pila.push(100)
pila.push(100)
pila.push(100)
pila.push(100)

pila.pop()

pila.show()

print("*" * 25)
print("Size: %d"%(pila.Size()))
print("Estado: %d"%(pila.empty()))
print("Top: %d"%(pila.Top()))