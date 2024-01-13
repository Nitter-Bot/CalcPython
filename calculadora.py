#Calculadora basica

#Menu
def menu():
    print("[1]Suma")
    print("[2]Resta")
    print("[3]Multiplicacion")
    print("[4]Division")
    print("[5]Potencia")
    print("[6]Salir\n")
    
print("Bienvenido, que deseas hacer?")
#Bucle
while(True):
    menu()
    opcion = int(input(" "))
    if opcion == 1:
        a=float(input("\nIngrese primer numero: "))
        b=float(input("Ingrese segundo numero: "))
        print(f" {a} + {b} =  {a+b} \n")
    elif opcion == 2:
        a=float(input("\nIngrese primer numero: "))
        b=float(input("Ingrese segundo numero: "))
        print(f" {a} - {b} = {a-b} \n")
    elif opcion == 3:
        a=float(input("\nIngrese primer numero: "))
        b=float(input("Ingrese segundo numero: "))
        print(f" {a} * {b} =  {a*b} \n")
    elif opcion == 4:
        a=float(input("\nIngrese primer numero: "))
        b=0
        while b==0:
            b=float(input("Ingrese segundo numero: "))
        print(f" {a} / {b} =  {a/b} \n")
    elif opcion == 5:
        a=float(input("\nIngrese primer numero: "))
        b=float(input("Ingrese segundo numero: "))
        print(f" {a} ^ {b} =  {a**b} \n")
    elif opcion == 6:
        print("\n Hasta luego!")
        break
    else:
        print("\nOpcion no valida intenta otra vez\n")