Algoritmo rollitos
	Escribir ""
	Escribir "******************* Rollitos *******************"
	Escribir ""
	Escribir "*************** Bienvenido *********************"
	Escribir "------ Promoción del día ------"
	Escribir "- Jarra de Jagger gratis"
	Escribir "- Si vienes con 3 amigos"
	Escribir "------------------------------------------------"
	
	Escribir "¿Cómo te llamas?"
	Leer nombre
	Escribir "¿Cuál es tu edad?"
	Leer edad
	Escribir "¿Con cuántas personas vienes?"
	Leer personas
	
	Si personas >= 3 Entonces
		Escribir "Tienes acceso a la promoción."
	SiNo
		Escribir "No tienes acceso a la promoción."
	FinSi
	
	Escribir "------------------------------------------------"
	Escribir "*************** Menú del día *******************"
	Escribir "1. Jarra de Jagger............ $6.50"
	Escribir "2. Jarra de Roncola........... $5.00"
	Escribir "3. Switch Tamarindo........... $4.00"
	Escribir "4. Cuba Libre................. $3.50"
	Escribir "------------------------------------------------"
	
	Escribir "¿Qué deseas comprar?"
	Leer bebida
	
	Escribir "Gracias por tu compra, ", nombre, ". ¡Disfruta tu bebida!"
FinAlgoritmo