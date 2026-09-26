def gestionar_tuplas():
    numeros_base = (28, 62, 98, 43, 51)
    numeros_capturados = ()

    for i in range(len(numeros_base)):
        if i == 2:
            print(f"Tercer elemento: {numeros_base[i]}")

    for _ in range(2):
        numero_ingresado = int(input("Ingresa otro número: "))
        numeros_capturados += (numero_ingresado,)

    todos_los_numeros = numeros_capturados + numeros_base
    lista_ordenada = sorted(todos_los_numeros)
    tupla_final = tuple(lista_ordenada)
    print(f"Tupla ordenada: {tupla_final}")

    def calcular_suma(coleccion):
        total_suma = 0
        for valor in coleccion:
            total_suma += valor
        return total_suma  

    resultado_suma = calcular_suma(tupla_final)
    print(f"La suma total de la tupla es: {resultado_suma}\n")

def gestionar_diccionario():
    agenda_contactos = {
        "Paulo": "889-653-424-524",
        "José": "337-452-781-921",
        "Jorge": "332-951-731-545"
    }

    nombre_nuevo = input("Nombre del nuevo contacto: ")
    telefono_nuevo = input("Teléfono del nuevo contacto: ")
    agenda_contactos[nombre_nuevo] = telefono_nuevo

    print("\n--- Lista de Contactos ---")
    for nombre in agenda_contactos:
        print(f"- {nombre}")

    def buscar_telefono(directorio, contacto):
        return directorio.get(contacto, "Contacto no encontrado")

    busqueda_nombre = input("\nNombre a buscar: ")
    telefono_hallado = buscar_telefono(agenda_contactos, busqueda_nombre)
    print(f"Teléfono de {busqueda_nombre}: {telefono_hallado}\n")

def gestionar_excepciones():
    try:
        primer_operando = int(input("Ingresa el primer número: "))
        segundo_operando = int(input("Ingresa el segundo número: "))

        resultado_suma = primer_operando + segundo_operando
        resultado_division = primer_operando / segundo_operando

        print(f"La suma es: {resultado_suma}")
        print(f"La división es: {resultado_division}\n")

    except ValueError:
        print("Error: Debes ingresar un número entero válido.\n")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero (0).\n")

def gestionar_strings():
    texto_base = " QUERIDAAA DIME CUANDO TU "

    print(f"Longitud del mensaje original: {len(texto_base)}")

    texto_mayusculas = texto_base.upper()
    print(f"Mensaje en mayúsculas: {texto_mayusculas}")

    texto_sanitizado = (
        texto_mayusculas
        .replace("QUERIDAAA", "DIME CUANDO")
        .replace("TU", "DIME CUANDO...")
    )
    print(f"Mensaje modificado:{texto_sanitizado}")

    def contar_palabras(frase):
        return len(frase.split())

    entrada_usuario = input("\nIngresa un nuevo texto: ")
    total_palabras = contar_palabras(entrada_usuario)
    print(f"El texto contiene {total_palabras} palabras.\n")

def ejecutar_menu_principal():
    opcion_seleccionada = ""
    
    while opcion_seleccionada != "5":
        print("========== MENÚ DE OPCIONES ==========")
        print("1. Ejercicio Tuplas")
        print("2. Ejercicio Diccionario")
        print("3. Ejercicio Excepciones")
        print("4. Ejercicio Strings")
        print("5. Salir")
        
        opcion_seleccionada = input("Selecciona una opción (1-5): ").strip()
        print("-" * 38)
        
        if opcion_seleccionada == "1":
            gestionar_tuplas()
        elif opcion_seleccionada == "2":
            gestionar_diccionario()
        elif opcion_seleccionada == "3":
            gestionar_excepciones()
        elif opcion_seleccionada == "4":
            gestionar_strings()
        elif opcion_seleccionada == "5":
            print("Cerrando el programa...")
        else:
            print("Opción inválida. Intenta nuevamente.\n")

ejecutar_menu_principal()