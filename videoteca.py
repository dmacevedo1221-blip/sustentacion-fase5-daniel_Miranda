

# Función para contar títulos que cumplen los criterios
def contar_titulos(matriz, umbral_calificacion, anio_limite):
    contador = 0
    for titulo in matriz:
        if titulo[2] >= umbral_calificacion and titulo[1] >= anio_limite:
            contador += 1
    return contador

# Crear matriz vacía
videoteca = []

# Pedir cantidad de títulos
n = int(input("¿Cuántos títulos desea ingresar? "))

# Ingreso de datos
for i in range(n):
    print(f"\nTítulo {i+1}:")
    nombre = input("Ingrese el título: ")
    anio = int(input("Ingrese el año de lanzamiento: "))
    calificacion = float(input("Ingrese la calificación (1-10): "))
    genero = input("Ingrese el género: ")
    
    videoteca.append([nombre, anio, calificacion, genero])

# Pedir criterios
umbral = float(input("\nIngrese el umbral de calificación: "))
anio_limite = int(input("Ingrese el año límite: "))

# Procesar
resultado = contar_titulos(videoteca, umbral, anio_limite)

# Mostrar resultado
print("\nCantidad de títulos que cumplen los criterios:", resultado)