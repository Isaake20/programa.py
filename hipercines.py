# Lista de ids secretas de los clientes frecuentes
Secreto = ["12345", "54321", "98765"]

print("""
    *********************************************************************************
    *                                                                               *
    *    H    H  IIIII  PPPPP   EEEEE  RRPRR   CCCCC  IIIII  N   N  EEEEE   SSSSS   *
    *    H    H    I    P   P   E      R   R   C        I    NN  N  E       S       *
    *    HHHHHH    I    PPPPP   EEEEE  RPRRR   C        I    N N N  EEEEE    SSSS   *
    *    H    H    I    P       E      R  R    C        I    N  NN  E           S   *
    *    H    H  IIIII  P       EEEEE  R   R   CCCCC  IIIII  N   N  EEEEE   SSSSS   *
    *                                                                               *
    *********************************************************************************
    """)
print("Bienvenid@")
print("--Promoción del día--")
print("Por la compra de 2 boletos, el tercero es gratis ")

# Puedo atender a varios clientes sin cerrar el programa
for i in range(1, 4):  
    print("----------------------------------------")
    print(f"\n=== CLIENTE {i} ===")

    nombre = input("¿Ayúdanos con tu nombre y apellido? \n")
    print("-----------------------------------")
    registro = input("¿Estás registrado si/no? \n").lower()

    if registro == "si":
        cedula = input("Ingresa tu cédula: \n")

        # Verificar si la cédula ingresada está en la lista de ids secretas
        if cedula in Secreto:
            print("-------------------------------------------------------")
            print(f"Bienvenido de nuevo: {nombre}")
            print("Tienes acceso a un 5% de descuento en tu compra\n ")
            print("---------------------------------------------------")
            personas = int(input("¿Con cuántas personas vienes?\n "))
            if personas >= 3:
                print("---------------------------------------")
                print("Tu tercer boleto tiene 50% de descuento")
                print("---------------------------------------\n")
            else:
                print("-------------------------------------------------------")
                print("No tienes acceso a la promoción, pero puedes continuar.")
                print("-------------------------------------------------------\n")
        else:
            print("Cédula incorrecta. No tienes acceso como cliente frecuente.\n")
    else:
        print("----------------------------------------\n")
        print(f"Bienvenido a Hipercines, {nombre}!\n")
        personas = int(input("¿Con cuántas personas vienes? \n"))
        print("----------------------------------------\n")
        if personas >= 3:
            print("Tienes acceso a la promoción del tercer boleto gratis \n")
            print("----------------------------------------\n")
        else:
            print("No tienes acceso a la promoción, pero puedes seguir adelante.\n")

    print("--------------------------------------")
    print("*Menú de Películas")
    print("1. Avengers: Endgame ........... $7.60")
    print("2. The Lion King ............... $7.60")
    print("3. Joker ....................... $3.25")
    print("4. Spider-Man: No Way Home .... .$7.60")
    print("--------------------------------------\n")

    pelicula = int(input("¿Qué película deseas ver? (Elige el número de la película): \n"))

    if pelicula == 1:
        precio_pelicula = 7.60
        nombre_pelicula = "Avengers: Endgame"
    elif pelicula == 2:
        precio_pelicula = 7.60
        nombre_pelicula = "The Lion King"
    elif pelicula == 3:
        precio_pelicula = 3.25
        nombre_pelicula = "Joker"
    elif pelicula == 4:
        precio_pelicula = 7.60
        nombre_pelicula = "Spider-Man: No Way Home"
    else:
        print("Opción inválida. Regresando al menú...\n")
        continue

    # Calculando el número de boletos
    boletos = personas  
    if personas >= 3:
        boletos = personas - 1 

    print(f"Necesitas {boletos} boletos para {personas} personas.\n")

    print("\n*Menú de Dulcería*")
    print("1. Combo Palomitas + Refresco..... $9.99")
    print("2. Hotdog + Gaseosa............... $7.50")
    print("3. Nachos + Refresco.............. $7.49")
    print("4. Solo Palomitas................. $6.00")
    print("----------------------------------------\n")

    combo = int(input("¿Qué deseas comprar? (Elige el número del combo): \n"))

    if combo == 1:
        precio_combo = 9.99
        producto = "Combo Palomitas + Refresco"
    elif combo == 2:
        precio_combo = 7.49
        producto = "Hotdog + Gaseosa"
    elif combo == 3:
        precio_combo = 7.49
        producto = "Nachos + Refresco"
    elif combo == 4:
        precio_combo = 6.00
        producto = "Solo Palomitas"
    else:
        print("----------------------------------------")
        print("Opción inválida. Regresando al menú...")
        print("----------------------------------------")
        continue

    print("------------------------------------------")
    cantidad_combos = int(input("¿Cuántas unidades deseas? "))
    print("------------------------------------------")
    total_combos = precio_combo * cantidad_combos

    # Aplicando descuento 
    descuento = 0
    if cedula in Secreto:
        descuento = 0.05  # Descuento del 5% para clientes frecuentes
        print(f"Descuento aplicado: 5%\n")

    total_combos_descuento = total_combos * (1 - descuento)  # Descuento en los combos

    factura = input("¿Deseas factura con tus datos personales? (si/no): ").lower()
    print("----------------------------------------------")

    if factura == "si":  
        print("------------------------------------------")
        direccion = input("Dime tu dirección: ")
        print("------------------------------------------")
        correo = input("Dime tu correo electrónico: ")
        print("------------------------------------------")
        telefono = input("Dime tu número de teléfono: ")
        print("------------------------------------------")
    else:
        direccion = "0000000000"
        correo = "0000000000000"
        telefono = "00000000000"

    iva = total_combos_descuento * 0.15
    total_combos_iva = total_combos_descuento + iva

    # Total de la compra: boletos + combos
    total_pagar = (boletos * precio_pelicula) + total_combos_iva

    print("======================================")
    print("********* FACTURA HIPERCINES *********")
    print("======================================")
    print(f"Nombre: {nombre}")
    print(f"Dirección: {direccion}")
    print(f"Correo: {correo}")
    print(f"Teléfono: {telefono}")
    print("--------------------------------------")
    print(f"Película: {nombre_pelicula}")
    print(f"Boletos: {boletos}")
    print(f"Producto: {producto}")
    print(f"Cantidad de combos: {cantidad_combos}")
    print("-----------------------------------------")
    print(f"Sub(Boletos): ${boletos * precio_pelicula:.2f}")
    print(f"Sub(Combos): ${total_combos_descuento:.2f}")
    print(f"IVA (15%): ${iva:.2f}")
    print(f"Total: ${total_pagar:.2f}")
    print("--------------------------------------")
    print(" Gracias por tu compra en HIPERCINES ")
    print("------------------------------------\n")

print("\nGracias por visitarnos, vuelve pronto \n")