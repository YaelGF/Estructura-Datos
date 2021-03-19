"""
    Elabora un codigo donde dada una palbra la
    invierta (usa la estructura de datos pila)
"""
def stringToList(string): 

    ls=[]#declaracion lista

    ls[:0]=string #pasar de str a lista

    return ls#retornar la variable ls
 
def listToString(string):  
    
    str1 = ""  #declaracion de string


    for i in string:#ciclo for

        str1 += i#concatenacion

    return str1 #retorno de la variable str1

def split(read):

    ls = []#declaracion de lista

    for i in range(len(read)):#ciclo for

        ls.append(read.pop())#agregar a la lista el ultimo valor de la lista read

    return ls#retorno de la variable ls

print(listToString(split(stringToList(input("Ingrese una plabra: ")))))#llamada de metodos