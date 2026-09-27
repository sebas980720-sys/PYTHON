"""#explicaciones:ciclo for repite cantidades de veces.

#mostra mensaje "hola mundo 10 veces 
mensaje =input("que mensaje quieres mostrar:")
cantidad = int(input("cuantas veces quiere repetir el mensaje"))

for i in range (cantidad):
    print(f"{mensaje}")


# Ejercicio 1: Mostrar la tabla de multiplicar de un número
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(20):          # recorre los valores del 1 al 10
    print(f"{numero} x {i+1} = {numero * i+1}")
     
# Ejercicio 2: Sumar los primeros n números naturales
n = int(input("Ingrese un número entero positivo: "))
uma = 0
for i in range(1, n + 1):
    suma = suma + i

print(f"La suma de los primeros {n} números naturales es: {suma}")


# ciclo for que repita 3 veces
import random 

numero_secreto = random.randint(1,10)
intentos = 3

for i in range(intentos):
    numero = int(input("adivina el numero secreto "))

    if numero == numero_secreto:
        print("¡felizidades! adivinaste el numero,")
        break
    else:
        intentos_restantes =intentos - (i + 1)
        print(f"te quedan {intentos - (i +1)}intentos,")

        if intentos_restantes == 0:
            print(f"el numero secreto era {numero_secreto}")



import random 

numero_secreto = random.randint(1,10)
intentos = 3

for i in range(intentos):
    numero = int(input("adivina el numero secreto "))

    if numero == numero_secreto:
        print("¡felizidades! adivinaste el numero,")
        break
    else:
        intentos_restantes =intentos - (i + 1)
        print(f"te quedan {intentos - (i + 1)}intentos,")

        if intentos_restantes == 0:
            print(f"el numero secreto era {numero_secreto}")

        # condicion diferente si el numero es mayor o menor ala variante
        if numero > numero_secreto :
            print("pista: muy alto,") 

        if numero < numero_secreto :
            print("pista: muy bajo,")    
"""