Algoritmo Discoteca_Selfie
Mientras Verdadero Hacer
        Escribir ""
        Escribir "Discoteca Selfie"
        Escribir ""
        Escribir "*Bienvenid@*"
        Escribir "--Promoción del día--"
        Escribir "Jarra de Jagger gratis"
        Escribir "Si vienes con 3 amigos"
        Escribir "----------------------"
		Escribir "¿Ayúdanos con tu nombre y apellido?"
        Leer nombre
		Escribir "-----------------------------------"
        Escribir "¿Estas registrado si/no?"
		leer registro
		Si registro = "si" Entonces
		Secreto = "1728695774"
		intentos = 1
		Mientras intentos <=3 Hacer
				Escribir "-----------------------------------"
				Escribir " ingresa tu cedula"
				leer cedula 
				Si cedula = Secreto Entonces
					Escribir "-------------------------------------------------------"
					Escribir " Bienvenido de nuevo: ", nombre
					Escribir " Tienes acceso una cuba libre por cliente frecuente"
					Escribir "---------------------------------------------------"
					Escribir "¿Con cuántas personas vienes?"
					Leer personas
					
					Si personas >= 3 Entonces
						
						Escribir "-----------------------------------"
						Escribir "Tienes acceso a la promoción."
					SiNo
						
						Escribir "------------------------------------------------"
						Escribir "No tienes acceso a la promoción, pero continuar."
					FinSi
					intentos = 4 
				SiNo
					Escribir " incorrecta "
					intentos = intentos +1
				Fin Si
			FinMientras
		SiNo
			Escribir "¿Cuál es tu edad?"
			Leer edad
			
			Si edad < 18 Entonces
				Escribir "Lo sentimos, debes ser mayor de edad para ingresar."
			FinSi
			
			Escribir "Bienvenido a Selfie ", nombre
			Escribir "¿Con cuántas personas vienes?"
			Leer personas
			
			Si personas >= 3 Entonces
				Escribir "Tienes acceso a la promoción."
			SiNo
				Escribir "No tienes acceso a la promoción, pero puedes seguir adelante."
			FinSi
		Fin Si
        Escribir "------------------------------------"
        Escribir "**  Menú del día  **"
        Escribir "1. Jarra de Jagger.......... $6.50"
        Escribir "2. Jarra de Roncola......... $5.00"
        Escribir "3. Switch Tamarindo......... $4.00"
        Escribir "4. Cuba Libre............... $3.50"
        Escribir "------------------------------------"
        Escribir "¿Qué deseas comprar? (Elige el número de la bebida)"
        Leer bebida
        Segun bebida Hacer
            1:
                precio = 6.5
                bebidaSelfie = "Jarra de Jagger"
			2:
                precio = 5.0
                bebidaSelfie = "Jarra de Roncola"
            3:
                precio = 4.0
                bebidaSelfie = "Switch Tamarindo"
            4:
                precio = 3.5
                bebidaSelfie = "Cuba Libre"
            De Otro Modo:
                Escribir "Opción inválida. Regresando al menú..."
                Esperar 2 Segundos
				
        FinSegun
        Escribir "¿Cuántas unidades deseas?"
        Leer cantidad
        total = precio * cantidad
        Escribir "------------------------------------------------"
        Escribir "¿Deseas factura con tus datos personales? (si/no)"
        Leer factura
        Si factura = "si" Entonces
            Escribir "Dime tu dirección:"
            Leer direccion
            Escribir "Dime tu correo electrónico:"
            Leer correo
            Escribir "Dime tu número de teléfono:"
            Leer telefono
        SiNo
            nombre = "00000000000000000000"
            direccion = "00000000000000000000"
            correo = "00000000000000000000"
            telefono = "00000000000000000000"
        FinSi
        Escribir "========================================"
        Escribir "**   FACTURA SELFIE   **"
        Escribir "========================================"
        Escribir "Nombre: ", nombre
        Escribir "Dirección: ", direccion
        Escribir "Correo: ", correo
        Escribir "Teléfono: ", telefono
        Escribir "----------------------------------------"
        Escribir "Producto: ", bebidaSelfie
        Escribir "Cantidad: ", cantidad
        Escribir "Precio unitario: $", precio
        Escribir "-----------------------------------------"
        Escribir "TOTAL : $", total
        iva = total * 0.15
        TotalIVa = total + iva
        Escribir "IVA (15%): $", iva 
        Escribir "Total a pagar: $", TotalIVa
        Escribir "-----------------------------------------"
        Escribir "Gracias por tu compra en Discoteca Selfie"
        Escribir "-----------------------------------------"
        Escribir "¿Deseas hacer otra compra? (si/no)"
        Leer opcion
        Si opcion = "no" Entonces
        FinSi
    FinMientras
    Escribir "Gracias por visitarnos, ¡vuelve pronto!"
FinAlgoritmo
