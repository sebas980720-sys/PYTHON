
"""
#Repaso clase pasada 
var_nombre = input("porfavor ingresar su nombre:")

#variable numerica 
var_edad =int(input(f"{var_nombre}porfavor ingrese su edad"))


#validar si la edad es > = 18 y mostrar un mensaje que diga que es mayor

if var_edad >=18:
    print(f"{var_nombre}usted es mayor de edad")


else:
    print(f"{var_nombre}usted es menor de edad")


# Ejercicio 1: Determinar si un número es positivo, negativo o cero
numero = float(input("Ingrese un número: "))

if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print("El número es cero")


 # Ejercicio 3: Determinar si un número es par o impar
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(f"el numero{numero} es par")
else: 
    print(f"el numero{numero} es impar ")   

# Ejercicio 4: Clasificar una nota académica
nota = float(input("Ingrese la nota obtenida (0.0 a 5.0): "))

if nota >5:
    print(f"(nota)invalida")
if nota >= 4.5:
    print("Desempeño superior")
elif nota >= 3.5:
    print("Desempeño alto")
elif nota >= 3.0:
    print("Desempeño básico")
elif:nota >=0 :
    print("Desempeño bajo")
else:
    print("nota invalida") 

# Ejercicio 5: Determinar el mayor de tres números
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2

elif n1 == n2 and n1==n3:
    mayor ="numeros iguales"
else:
    mayor = n3

print(f"El mayor de los tres números es: {mayor}")



#Ejercicio 4: Condicionales clima

var_ciudad = input("\nIngrese la CIUDAD: ")

var_grados = float(input("\nIngrese grados celsius:"))

if var_grados >32:
    print (f"{var_ciudad} Esta MUY CALIENTE , la temperatura es de {var_grados}° grados celsius")

elif var_grados >=26 and var_grados <=32:
    print (f"{var_ciudad} Esta CALIENTE , la temperatura es de {var_grados}° grados celsius")

elif var_grados >=18 and var_grados <=25:
    print (f"{var_ciudad} Esta TEMPLADO , la temperatura es de {var_grados}° grados celsius")

elif var_grados >=10 and var_grados <=17:
    print (f"{var_ciudad} Esta FRIA, se recominda usar ABRIGO , la temperatura es de {var_grados}° grados celsius")

elif var_grados <10:
    print (f"{var_ciudad} Esta MUY FRIO, se recominda usar ABRIGO , la temperatura es de {var_grados}° grados celsius")



  # Ejercicio 2
print("Notas Finales de los estudiantes")

variable_nombre= input("Por favor ingrese su nombre: ")
var_calificacion= float(input("Ingrese su calificación: "))
if var_calificacion >= 4.5 and var_calificacion <= 5.0:
    resultado = "Aprobó"
    desempeño = "Excelente"
    print(f"Estudiante: {variable_nombre} | Calificación: {var_calificacion} | Resultado: {resultado} | Desempeño: {desempeño}")
elif var_calificacion >= 3.5 and var_calificacion < 4.5:
    resultado = "Aprobó"
    desempeño = "Bueno"
    print(f"Estudiante: {variable_nombre} | Calificación: {var_calificacion} | Resultado: {resultado} | Desempeño: {desempeño}")
elif var_calificacion >= 3.0 and var_calificacion < 3.5:
    resultado = "Aprobó"
    desempeño = "Aceptable"
    print(f"Estudiante: {variable_nombre} | Calificación: {var_calificacion} | Resultado: {resultado} | Desempeño: {desempeño}")
elif var_calificacion >=0.0 and var_calificacion < 3.0:
    resultado = "Reprobó"
    desempeño = "Insuficiente"
    print(f"Estudiante: {variable_nombre} | Calificación: {var_calificacion} | Resultado: {resultado} | Desempeño: {desempeño}")
else: 
    print(f"{var_calificacion} es inválida")


"""



