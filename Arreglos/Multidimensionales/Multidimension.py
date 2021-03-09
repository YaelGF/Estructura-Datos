#Declaracion
multi = [[[1,2,3],[4,5,6]],
        [[6,5,4],[3,2,1]]]
#Declaracion ejemplo 2:
'''
    a= [1,2]
    b=[2,3]
    c= [a,b]
    a2=[ 4,5]
    b2=[5,6]
    c2=[a2,b2]
    multi = [c, c2]
'''

#impresion total
print(multi)

print("********************")

#impresion de valor en posicion especifica
print(multi[0][1][2])

print("********************")

#Visualizar contenido del vector de Matrices
for i in range(len(multi)):
    for j in range(len(multi[i])):
        for k in range (len(multi[i][j])):
            print(multi[i][j][k])