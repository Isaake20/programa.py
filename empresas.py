#control de temperatura
    # valor de sueldos (diarios, mensuales anuales)
    # calculo de areas y perimetros de 4 figuras basicas 
import math


print("----------------------")
print("--------Famit---------")
print("----------------------")
print("---Menu de opciones---")
print("1. Control de temperutura")
print("2. Calculo de sueldos")
print("3. calculo de areas y perimetros")
print("-------------------------")
pregunta = float(input("Que deseas realizar: "))
if pregunta == 1:
    print("----------------------------")
    print("1. Control de temperutura")
    grados = float(input("ingrese la temperatura en celsius: "))
    gradosF = (grados* 9/5) + 32
    print(grados, ("°C") )
    print(gradosF, (".2°F"))
    
if pregunta == 2:
    print("----------------------------------")
    print("2. Calculo de sueldos")
    sueldo = float(input("ingresa el valor de cada hora: "))
    diario = (sueldo * 8)
    mensual = (diario * 20)
    anual = (mensual * 12)
    print(" tu sueldo diario es", diario)
    print(" tu sueldo mensual es", mensual)
    print(" tu sueldo anual es", anual)
      
if pregunta == 3:
    print("---------------------------------")
    print("3. calculo de areas y perimetros")
    print("---------------------------------")
    print(" Que figura deseas calcular: ")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Triangulo")
    print("4. Circulo")
    print("---------------------------------")
    figura = int(input("Que figura deseas realizar: "))
    if figura == 1:
        lado = int(input("ingrese la lngitud del lado cuadrado  "))
        area = lado ** 2
        perimetro = 4 * lado
        print("Área del cuadrado: ", area )
        print("Perímetro del cuadrado: ", perimetro)
        
    elif figura == 2:
        largo = float(input("ingrese el largo del rectangulo "))
        ancho = float(input("ingrese ancho del rectangulo "))
        area = largo * ancho
        perimetro = 2 * (largo + ancho)
        print("Área del rectángulo: ", area )
        print("Perímetro del rectángulo: ",perimetro)
    elif figura == 3:
        radio = float(input("Ingrese el radio del círculo: "))
        area = math.pi * (radio ** 2)
        perimetro = 2 * math.pi * radio
        print(f"Área del círculo: {area:.2f}")
        print(f"Perímetro del círculo: {perimetro:.2f}")
    elif figura == 4:
        print(" Que figura deseas calcular: ")
    elif figura >= 5:
        print(" no existe la opcion")
    
        
    else:
        print ("opcion incorrecta, adios ")