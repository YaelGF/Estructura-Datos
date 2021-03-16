from cola import Cola
from os import system

system("clear")

cola = Cola()

cola.push(12)
cola.push(14)
cola.push(15)
cola.push(16)
cola.push(17)

cola.show()

cola.popi()

print("*"*25)

cola.show()