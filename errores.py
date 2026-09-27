"""
try: 
    numero= int(input("ingrese un numero:"))
    print(f"el numero ingresado es: {numero}")
except ValueError:
    print("por favor, ingrese un numero valido.")
    """



menu =0

        
while menu != 3:

    try:
        menu=int(input("""
        seleccione una opcion:
        1.sumar
        2.restar
        3.salir

        :

        """))
            
        if menu == 1:
                
                n1=int(input("ingrese el primer numero:"))
                n2=int(input("ingrese el segundo numero:"))
                print(f"la suma es: {n1+n2}")
        elif menu == 2:
                n1=int(input("ingrese el primer numero:"))
                n2=int(input("ingrese el segundo numero:"))
                print(f"la resta es: {n1-n2}")
        else:
                print("opcion invalida")   

    except ValueError:
        print("por favor, ingrese un numero valido.") 

        print("saliendo del sistema...")


