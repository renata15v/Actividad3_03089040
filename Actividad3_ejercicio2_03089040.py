print("Ejercicio 2: Menú de la Cafetería Cute")
print("Nombre: Renata Zoé Valdés García")
print("Matrícula: al03089040")

# while True: el menú se repite siempre; la única salida es el break 
while True:
    # Mostramos el menú
    print("==== Cafetería Cute ====")
    print("1. Ver bebidas")
    print("2. Ver postres")
    print("3. Ver horario")
    print("4. Salir")

    # Pedimos la opción
    opcion = input("Elige una opción:  ")

    # Revisamos qué opción eligió
    if opcion == "1":
        print("Frappé de fresa . . . . $65")
        print("Chai . . . . $45")
        print("Smoothie de mango . . . . $55")
    elif opcion == "2":
        print("Galleta de chocolate . . . $35")
        print("Cupcake red velvet . . . $25")
        print("Dona glaseada . . . . $30")
    elif opcion == "3":
        print("Lunes a viernes: 7:00 a 20:00")
        print("Sábados: 9:00 a 15:00")
    elif opcion == "4": 
        print("¡Gracias por visitarnos!")
    # El cliente eligió salir: break nos saca del while break
    else:
        print("Opción no válida, elige del 1 al 4")



