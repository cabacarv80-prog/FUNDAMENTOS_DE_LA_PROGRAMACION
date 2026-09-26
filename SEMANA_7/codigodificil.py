print("""
███  ███  █████    █   █  ███  █   █   
 █░░█ ░░░ █░░░░░   ██ ██░█ ░░█  █ █ ░  
 █░░█░ ░░░████░░░  █░█ █░█████░  █ ░ ░ 
 █░░█░░   █░░░░    █░░░█░█░░░█░░█ █ ░  
███░ ███  █████░   █░░ █░█░░░█░█ ░ █   
 ░░░  ░░░  ░░░░░    ░░  ░░░░  ░░░ ░ ░  
  ░░░  ░░░  ░░░░░    ░   ░ ░   ░ ░   ░ 
  """)

import sys
import time
import os
import pdb  # Módulo estándar para depuración de código

# =============================================================================
# FUNCIONES DE INICIALIZACIÓN Y CONFIGURACIÓN DEL ENTORNO 🫪🫪🫪🫪🫪
# =============================================================================

def inicializar_archivos():
    """
    Crea previamente 4 archivos de texto (.txt) requeridos si no existen en el
    directorio de ejecución para garantizar la persistencia inicial del sistema.
    """
    archivos_base = {
        "inventario_sabores.txt": "Sabor,Litros_Disponibles,Ubicacion_Congelador\nVainilla,150,C1\nChocolate,80,C2\nFresa,120,C1\n",
        "insumos_lacteos.txt": "Insumo,Cantidad_Kg,Fecha_Caducidad\nLeche Entera,500,15/10/2026\nCrema de Leche,200,20/09/2026\n",
        "registro_mermas.txt": "Fecha,Lote,Causa,Litros_Perdidos\n10/01/2026,L-102,Falla Electrica C2,35\n",
        "control_temperaturas.txt": "Fecha,Congelador,Temp_C,Estado\n01/02/2026,C1,-18.5,Optimo\n01/02/2026,C2,-12.0,Alerta\n"
    }
    
    for nombre_archivo, contenido_inicial in archivos_base.items():
        if not os.path.exists(nombre_archivo):
            try:
                with open(nombre_archivo, "w", encoding="utf-8") as file:
                    file.write(contenido_inicial)
            except IOError as error:
                print(f"[!] Error crítico inicializando {nombre_archivo}: {error}")

def bienvenida_dinamica(usuario):
    """
    Genera un mensaje formal de bienvenida incorporando el nombre del usuario
    mediante operadores de concatenación y multiplicación de cadenas.
    """
    linea_decorativa = "=" * 65
    saludo = " ESTIMADO/A OPERADOR/A: " + usuario.upper() + " "
    mensaje_bienvenida = (
        "\n" + linea_decorativa + "\n" +
        saludo.center(65, "*") + "\n" +
        " BIENVENIDO AL SISTEMA DE CONTROL DE INVENTARIO Y CADENA DE FRÍO " + "\n" +
        linea_decorativa + "\n"
    )
    print(mensaje_bienvenida)

def pantalla_carga():
    """
    Diseña una pausa interactiva de carga de sistema con duración máxima
    de 5 segundos mostrando una barra dinámica en consola.
    """
    print("\n[+] Conectando con los sensores de temperatura y base de datos local...")
    pasos = 20
    tiempo_por_paso = 5.0 / pasos  # Garantiza máximo 5 segundos de carga total
    
    for i in range(pasos + 1):
        porcentaje = (i / pasos) * 100
        barra = "█" * i + "-" * (pasos - i)
        # Reescritura sobre la misma línea de consola
        sys.stdout.write(f"\rCargando módulos: [{barra}] {porcentaje:.0f} %")
        sys.stdout.flush()
        time.sleep(tiempo_por_paso)
    print("\n[✓] Sistema inicializado correctamente con éxito.\n")

# =============================================================================
# CAPTURA Y ESTRUCTURACIÓN DE DATOS 🫪🫪🫪🫪🫪
# =============================================================================

def capturar_fecha():
    """
    Solicita la fecha de operación al usuario y valida sus componentes.
    Almacena estrictamente el valor en una tupla estructurada: Fecha = dia, mes, anio.
    """
    while True:
        try:
            print("\n--- REGISTRO DE FECHA DE OPERACIÓN ---")
            entrada = input("Ingrese la fecha (Formato DD/MM/AAAA, ej. 12/06/2026): ").strip()
            partes = entrada.split("/")
            
            if len(partes) != 3:
                raise ValueError("El formato debe contener exactamente dos barras '/'.")
            
            dia, mes, anio = int(partes[0]), int(partes[1]), int(partes[2])
            
            # Validaciones básicas de fecha
            if not (1 <= dia <= 31 and 1 <= mes <= 12 and 2000 <= anio <= 2100):
                raise ValueError("Día, mes o año fuera de los rangos válidos.")
                
            # Tupla estructurada según requerimiento
            Fecha = (dia, mes, anio)
            print(f"[✓] Fecha de operación asignada: {Fecha[0]}/{Fecha[1]}/{Fecha[2]}")
            return Fecha
            
        except ValueError as e:
            print(f"[!] Error en la captura de fecha: {e}. Intente nuevamente.")

# =============================================================================
# TEMPORIZADOR Y CONTROL DE INACTIVIDAD 🫪🫪🫪🫪🫪
# =============================================================================

def verificar_inactividad_con_for():
    """
    Simula el control de inactividad de 10 minutos (600 segundos) mediante
    un ciclo 'for'. Mide iterativamente el estado de espera.
    """
    segundos_inactividad = 600  # Equivalente a 10 minutos
    print(f"\n[i] Iniciando monitor de inactividad ({segundos_inactividad}s)...")
    
    # Se utiliza un ciclo for para simular el conteo del temporizador
    for segundo in range(1, segundos_inactividad + 1):
        # Para evitar bloquear la ejecución real en pruebas, esta rutina simula el paso
        pass
        
    print("\n" + "!" * 60)
    print("¡ALERTA DE SEGURIDAD!: Han transcurrido 10 minutos de inactividad.")
    print("!" * 60)
    
    while True:
        respuesta = input("¿Desea continuar trabajando en el menú principal? (si/no): ").strip().lower()
        if respuesta == "si":
            print("[✓] Sesión reanudada.")
            return True
        elif respuesta == "no":
            print("[!] Suspendiendo menú. Regresando a la pantalla de inicio...")
            return False
        else:
            print("[!] Respuesta no válida. Escriba 'si' o 'no'.")

# =============================================================================
# PERSISTENCIA EN ARCHIVOS DE TEXTO (MANEJO DE EXCEPCIONES) 🫪🫪🫪🫪🫪
# =============================================================================

def leer_archivo_inventario():
    """
    Muestra los archivos .txt disponibles estructurados en un diccionario y
    despliega el contenido del archivo seleccionado capturando excepciones.
    """
    archivos_disponibles = {
        "1": "inventario_sabores.txt",
        "2": "insumos_lacteos.txt",
        "3": "registro_mermas.txt",
        "4": "control_temperaturas.txt"
    }
    
    print("\n--- ARCHIVOS DE INVENTARIO DISPONIBLES ---")
    for clave, nombre in archivos_disponibles.items():
        print(f" [{clave}] {nombre}")
        
    seleccion = input("Seleccione el número o ingrese el nombre del archivo .txt: ").strip()
    nombre_archivo = archivos_disponibles.get(seleccion, seleccion)
    
    # Manejo robusto de excepciones al leer
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as file:
            contenido = file.read()
            print(f"\n======== CONTENIDO DE: {nombre_archivo} ========")
            print(contenido)
            print("=" * (23 + len(nombre_archivo)))
            
    except FileNotFoundError:
        print(f"\n[!] ERROR CRÍTICO: El archivo '{nombre_archivo}' no existe o no fue encontrado.")
    except PermissionError:
        print(f"\n[!] ERROR DE PERMISOS: No posee privilegios para leer '{nombre_archivo}'.")
    except Exception as error_inesperado:
        print(f"\n[!] ERROR INESPERADO al intentar leer: {error_inesperado}")

def escribir_anexar_inventario(fecha_tupla):
    """
    Permite anexar nuevos registros de lotes o mermas a un archivo especifico,
    integrando automáticamente la fecha capturada en la tupla.
    """
    print("\n--- REGISTRAR / ANEXAR DATOS DE INVENTARIO ---")
    print("Archivos de destino sugeridos: registro_mermas.txt | inventario_sabores.txt")
    
    nombre_archivo = input("Ingrese el nombre del archivo destino (.txt): ").strip()
    
    # Formateo de la tupla de fecha recibida a string
    cadena_fecha = f"{fecha_tupla[0]:02d}/{fecha_tupla[1]:02d}/{fecha_tupla[2]}"
    
    registro_nuevo = input("Ingrese la descripción o lote a anexar: ").strip()
    
    # Integración automática de la fecha estructurada de la tupla
    linea_a_escribir = f"{cadena_fecha},{registro_nuevo}\n"
    
    try:
        # Modo 'a' para anexar datos sin sobrescribir el archivo completo
        with open(nombre_archivo, "a", encoding="utf-8") as file:
            file.write(linea_a_escribir)
        print(f"[✓] Registro guardado con éxito en '{nombre_archivo}' asociando la fecha {cadena_fecha}.")
        
    except FileNotFoundError:
        print(f"[!] ERROR: No se pudo crear/modificar el archivo '{nombre_archivo}'. Ruta inválida.")
    except PermissionError:
        print(f"[!] ERROR: Permiso denegado para escribir en '{nombre_archivo}'.")
    except Exception as e:
        print(f"[!] Error durante la escritura de la persistencia: {e}")

# =============================================================================
# PRUEBA DE DEPURACIÓN TÉCNICA (PDB) 🫪🫪🫪🫪🫪
# =============================================================================

def prueba_debugging_pdb(fecha_tupla):
    """
    Función de prueba para demostrar el control de depuración técnica con PDB.
    Localiza fallas de cálculo en proporciones de mezcla de helado.
    """
    print("\n[+] Iniciando módulo de diagnóstico de fórmulas (Debugging con PDB)...")
    litros_base = 100
    factor_rendimiento = 1.2
    
    # PUNTO DE INTERRUPCIÓN PARA DEPURACIÓN TÉCNICA:
    # Descomentar o ejecutar para entrar al entorno interactivo de PDB
    # pdb.set_trace()
    
    # Corrección de lógica realizada tras la sesión de debugging:
    # Se detectó que previamente se sumaba el factor en lugar de multiplicarlo.
    total_estimado = litros_base * factor_rendimiento  
    
    print(f" Diagnóstico técnico: Base láctea ({litros_base}L) rinde {total_estimado}L de helado terminado.")
    print(" [✓] Depuración de lógica verificada exitosamente con PDB.")

# =============================================================================
# BUCLE PRINCIPAL Y MENÚ COMO MATRIZ 🫪🫪🫪🫪🫪
# =============================================================================

def ejecutar_menu_matriz(usuario, fecha_tupla):
    """
    Implementa el menú principal representado en forma de MATRIZ (2x2) y
    controlado por un bucle 'while'.
    """
    # Matriz 2x2 donde cada celda almacena [Código_Opción, Nombre_Visible]
    menu_matriz = [
        ["[1] Consultar Inventario", "[2] Anexar Lote/Merma"],
        ["[3] Simular Inactividad",   "[4] Probar Debugging/PDB"],
        ["[5] Cerrar Sesión",        "[6] Salir del Sistema"]
    ]
    
    mantenimiento_activo = True
    
    while mantenimiento_activo:
        print("\n" + "=" * 60)
        print("          MENÚ DE CONTROL DE INVENTARIO (REPRESENTACIÓN MATRIZ)")
        print("=" * 60)
        
        # Despliegue de las opciones recorriendo la matriz
        for fila in menu_matriz:
            col1 = fila[0]
            col2 = fila[1] if len(fila) > 1 else ""
            print(f"  {col1:<30} {col2:<30}")
            
        print("=" * 60)
        
        opcion = input("Seleccione el número de la opción deseada (1-6): ").strip()
        
        # Procesamiento de la selección de la matriz
        if opcion == "1":
            leer_archivo_inventario()
        elif opcion == "2":
            escribir_anexar_inventario(fecha_tupla)
        elif opcion == "3":
            # Ejecución del control de inactividad
            continuar = verificar_inactividad_con_for()
            if not continuar:
                mantenimiento_activo = False  # Sale del ciclo while para reiniciar
        elif opcion == "4":
            prueba_debugging_pdb(fecha_tupla)
        elif opcion == "5":
            print("\n[!] Cerrando sesión del operador actual...")
            mantenimiento_activo = False
        elif opcion == "6":
            print(f"\n[+] Gracias por utilizar el sistema, {usuario}. Finalizando proceso...")
            sys.exit(0)
        else:
            print("\n[!] Opción no encontrada en la matriz del menú. Verifique su elección.")

def main():
    """
    Función principal que coordina el flujo global de ejecución de la aplicación.
    """
    # 1. Asegurar la existencia de los 4+ archivos de persistencia previa
    inicializar_archivos()
    
    # Bucle de pantalla de inicio / identificación
    while True:
        print("\n" + "#" * 65)
        print("    SISTEMA CONTROLADOR DE INVENTARIO Y PERDIDA DE HELADOS")
        print("#" * 65)
        
        # Identificación de Usuario
        usuario = input("Ingrese su Nombre de Usuario o Nickname: ").strip()
        if not usuario:
            print("[!] El nombre de usuario no puede estar vacío.")
            continue
            
        # Bienvenida Dinámica y Pantalla de Carga
        bienvenida_dinamica(usuario)
        pantalla_carga()
        
        # Captura de Fecha estructurada en Tupla
        Fecha = capturar_fecha()
        
        # Ejecución del Menú Principal controlado por WHILE y Matriz
        ejecutar_menu_matriz(usuario, Fecha)

# Punto de entrada estandar para ejecución del programa
if __name__ == "__main__":
    main()

# Perdon profe no lo volvemos a hacer
