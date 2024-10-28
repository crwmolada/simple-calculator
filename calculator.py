def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b): return a / b if b != 0 else "Indefinido (división por cero)"
def potencia(a, b): return a ** b
def divisionalpiso(a, b): return a // b if b != 0 else "Indefinido (división por cero)"
def modulo(a, b): return a % b

print("Bienvenido al programa calculadora")


lista_historial = []

while True:
    # Se muestra menú
    print("\nSeleccione una operación:")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) División al piso")
    print("6) Módulo")
    print("7) Potencia")

    # Solicitamos opción
    try:
        opcion = int(input("Ingrese una opción (0 para salir): "))
    except ValueError:
        print("Por favor, ingrese un número válido para la opción.")
        continue 
    
    if opcion == 0:
        print("Hasta luego!")
        break 
    lista_historial.append(opcion)

    # Bucle para solicitar valores válidos para `a` y `b`
    while True:
        try:
            a = int(input("Ingrese un número x: "))
            b = int(input("Ingrese un número y: "))
            break 
        except ValueError:
            print("Por favor, ingrese números válidos para x e y.")

    # Realiza la operación según la opción ingresada
    if opcion == 1:
        print("La suma de " + str(a) + " + " + str(b) + " es: " + str(suma(a, b)))
    elif opcion == 2:
        print("La resta de " + str(a) + " - " + str(b) + " es: " + str(resta(a, b)))
    elif opcion == 3:
        print("La multiplicación de " + str(a) + " * " + str(b) + " es: " + str(multiplicacion(a, b)))
    elif opcion == 4:
        print("La división de " + str(a) + " / " + str(b) + " es: " + str(division(a, b)))
    elif opcion == 5:
        print("La división al piso de " + str(a) + " // " + str(b) + " es: " + str(divisionalpiso(a, b)))
    elif opcion == 6:
        print("El módulo de " + str(a) + " % " + str(b) + " es: " + str(modulo(a, b)))
    elif opcion == 7:
        print("La potencia de " + str(a) + " ** " + str(b) + " es: " + str(potencia(a, b)))
    else:
        print("Opción no válida")

if any(1 <= i <= 7 for i in lista_historial):  # Verificar si hubo operaciones válidas
    lista_conteo = [0, 0, 0, 0, 0, 0, 0]
    for i in lista_historial:
        if 1 <= i <= 7:
            lista_conteo[i - 1] += 1
    
    # Mostrar el historial y el conteo de operaciones
    print("\nHistorial de opciones ingresadas:", lista_historial)
    print("Conteo de cada operación realizada:", lista_conteo)
else:
    print("\nNo se realizaron operaciones.")
