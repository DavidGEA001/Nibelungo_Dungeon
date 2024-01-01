print("BIENVENIDO AL LABERINTO DEL NIVELUNGO")

tenemosllave = False

puertaabierta = False

codigoconseguido = False

posiciondeljugador = "centro"

while (True):


    # SALA CENTRAL
    if posiciondeljugador == "centro":
        print ("ESTAS EN LA SALA CENTRAL")
        print("OPCIONES")
        print ("--izquierda")
        print ("--derecha")
        Seleccion = input("Selecciona una opcion: ")
        if Seleccion == "izquierda":
            posiciondeljugador = "izquierda"
        elif Seleccion == "derecha":
            posiciondeljugador = "derecha"
        else:
            print ("Opcion incorrecta")


    # SALA DE LA LLAVE
    if posiciondeljugador == "izquierda":
        print ("ESTAS EN LA SALA DE LA IZQUIERDA")
        print("OPCIONES")
        print ("--derecha")
        if tenemosllave == False:
            print ("--obtener (Llave detectada)")
        Seleccion = input("Selecciona una opcion: ")
        if Seleccion == "derecha":
            posiciondeljugador = "centro"
        elif Seleccion == "obtener":
            if tenemosllave == False:
               Codigo= input("Ingresa el codigo ")
               if Codigo == "4779":
                    tenemosllave = True
                    print("LLAVE OBTENIDA")
               else:
                   print ("Codigo incorrecto")

        else:
            print ("Opcion incorrecta")


    # SALA DE LA DERECHA
    if posiciondeljugador == "derecha":
        print ("ESTAS EN LA SALA DE LA DERECHA")
        print("OPCIONES")
        print ("--izquierda")
        print ("--subir escaleras")
        if tenemosllave == True:
            print ("--Usar llave (Puerta detectada)")
        Seleccion = input("Selecciona una opcion: ")
        if Seleccion == "izquierda":
            posiciondeljugador = "centro"
        elif Seleccion == "subir escaleras":
            posiciondeljugador = "segundo piso"
        elif Seleccion == "usar llave" and tenemosllave == True:
            print ("¡FELICIDADES HAZ SALIDO DEL LABERINTO!")
            exit()

        else:
            print ("Opcion incorrecta")


    # SEGUNDO PISO
    if posiciondeljugador == "segundo piso":
        print ("ESTAS EN EL SEGUNDO PISO")
        print("OPCIONES")
        print ("--bajar escaleras")
        print ("--ver (Papel sospechozo)")
        Seleccion = input("Selecciona una opcion: ")
        if Seleccion == "bajar escaleras":
            posiciondeljugador = "derecha"
        elif (Seleccion == "ver" and codigoconseguido == False):
            print ("El Codigo es 4779")
            print ("CODIGO OBTENIDO")
            codigoconseguido = True
        elif codigoconseguido == True:
                print ("Ya tienes el codigo")
        else:
            print ("Opcion incorrecta")






