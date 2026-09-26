# ACTIVIDAD EVALUABLE 3: TABLA DE PITÁGORAS EN MATRIZ Y OPERACIONES ESPECIALES

matriz = []
for i in range(1, 11):
    fila = []
    for p in range(1, 11):
        fila.append(i * p)
    matriz.append(fila)

for fila in matriz:
    for elemento in fila:
        print(f"{elemento:4}", end="") 
    print()

fila = int(input("coordenada1: "))
columna = int(input("coordenada2: "))
resultados = matriz[fila -1][columna -1]

print(f"el resultado es: ({fila},{columna}){resultados}")