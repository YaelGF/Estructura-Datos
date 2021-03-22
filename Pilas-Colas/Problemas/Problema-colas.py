answer2 = "s"
while answer2 == "s":  
  lsclientes = []
  lskilos = []

  clientes = int(input("Cuantas personas hay formadas? "))

  for i in range(clientes):
    name = input("ingrese su nombre: ")
    pedido = input("igrese cuantos kilos va a querer: ")

    lsclientes.append(name)
    lskilos.append(pedido)

  answer = "s"
  n = 0

  while answer == "s" and n <= len(lsclientes)+1:
    print("va el cliente ", lsclientes.pop(0))
    print("quiere: ", lskilos.pop(0), " kilos" )

    answer = input("siguiente?(s/n) ")
    n += 1

  print("Se acabaron :D")
  answer2 = input("Desea agregar mas?(s/n) ")