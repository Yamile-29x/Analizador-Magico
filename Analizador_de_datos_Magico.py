import csv

def cargar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            datos = list(lector)
        print("Datos cargados correctamente.")
        return datos
    except FileNotFoundError:
        print(" Archivo no encontrado.")
        return []

def mostrar_menu():
    print("\n MENÚ ANALIZADOR DE DATOS MÁGICO")
    print("1. Filtrar datos")
    print("2. Calcular estadísticas")
    print("3. Aplicar transformaciones")
    print("4. Guardar resultados")
    print("5. Salir")

def filtrar_datos(datos, campo, valor_minimo):
    try:
        return [fila for fila in datos if float(fila[campo]) >= float(valor_minimo)]
    except ValueError:
        print(" Error: asegúrate de que los datos sean numéricos.")
        return []

def calcular_estadisticas(datos, campo):
    try:
        numeros = [float(fila[campo]) for fila in datos]
        promedio = sum(numeros) / len(numeros)
        print(f" Promedio de {campo}: {promedio:.2f}")
        print(f" Total de registros: {len(numeros)}")
    except ValueError:
        print(" Error: asegúrate de que los datos sean numéricos.")

def transformar_datos(datos, campo):
    for fila in datos:
        fila[campo] = fila[campo].upper()
    print(f" Transformación aplicada: {campo} a mayúsculas.")
    return datos

def guardar_datos(datos, nombre_archivo):
    if not datos:
        print("⚠ No hay datos para guardar.")
        return
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        campos = datos[0].keys()
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)
    print(f" Datos guardados en {nombre_archivo}")

# Programa principal
def main():
    nombre_archivo = input(" Ingresa el nombre del archivo CSV a cargar: ")
    datos = cargar_datos(nombre_archivo)
    datos_filtrados = datos  # Para trabajar sobre una copia modificable

    while True:
        mostrar_menu()
        opcion = input(" Elige una opción: ")

        if opcion == '1':
            campo = input(" Campo a filtrar: ")
            valor = input(" Valor mínimo: ")
            datos_filtrados = filtrar_datos(datos, campo, valor)
        elif opcion == '2':
            campo = input(" Campo para calcular estadísticas: ")
            calcular_estadisticas(datos_filtrados, campo)
        elif opcion == '3':
            campo = input(" Campo a transformar a mayúsculas: ")
            datos_filtrados = transformar_datos(datos_filtrados, campo)
        elif opcion == '4':
            nombre_salida = input(" Nombre del nuevo archivo CSV: ")
            guardar_datos(datos_filtrados, nombre_salida)
        elif opcion == '5':
            print(" ¡Hasta luego!")
            break
        else:
            print(" Opción no válida.")

if __name__ == "__main__":
    main()
