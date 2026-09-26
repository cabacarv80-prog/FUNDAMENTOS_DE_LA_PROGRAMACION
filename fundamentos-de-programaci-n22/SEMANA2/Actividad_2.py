# DESCRIPCIÓN DEL RETO
preciomenor = 30
precioadulto = 45
descadultomayor = 0.12
descprofe = 0.10
descestu = 0.10
personas = int(input("Cuantas personas nos visitan? "))
total = 0

for c in range(1, personas + 1):
    while True:
        edad = int(input(f"Ingresa la edad de la persona {c}: "))
        if edad < 0:
            print("Edad inválida")
            continue
        break

    descuento = 0
    tipo = "sin descuento"
    if edad <3:
        preciobase = 0
        total = 0
        print("Pasa gratis")
    elif edad <= 17:
        preciobase = preciomenor
        estudiante = input("Eres estudiante= si/no")
        while estudiante != "si" and estudiante != "no":
            print("Respuesta invalida, vuelva a intentarlo")
            estudiante = input("Eres estudiante? si/no ")
        if estudiante == "si":
            descuento = descestu
            tipo = "estudiante"
        total = preciobase - (preciobase * descuento)
    else:
        preciobase = precioadulto
        tipodevisitante = input("es profesor, estudiante, adulto mayor u otro?")
        while (tipodevisitante != "profesor" and tipodevisitante != "estudiante" and tipodevisitante != "adulto mayor" and tipodevisitante != "otro"):
            print("tipo de visitante invalido, vuelve a intentarlo")
            tipovisitante = input("es profesor, estudiante, adulto mayor u otro? ")
        if tipodevisitante == "adulto mayor":
            descuento = descadultomayor
            tipo = "adulto mayor"
        elif tipodevisitante == "profesor":
            descuento = descprofe
            tipo = "profesor"
        elif tipodevisitante == "estudiante":
            descuento = descestu
            tipo = "estudiante"
        total = preciobase - (preciobase * descuento)

    montodescuento = preciobase * descuento
    totalgeneral = totalgeneral + total

    print("Tabla")
    print(f"Persona {c}")
    print(f"Edad: {edad}")
    print(f"Tipo: {tipo}")
    print(f"Precio base: $ {montodescuento}")
    print(f"Total a pagar: ${total}")
print(f"Total de todas las personas ${total}")
