from functions import *

NameFun = [sumar, restar, multiplicar, dividir]

print("-----Calculadora----- \n  \nFunciones:")

for i in NameFun:
    print("  " + i.__name__)

userFun = str(input("\nIngrese la función que desea realizar: "))
primero = int(input("ingrese el 1er digito: "))
segundo = int(input("ingrese el 2do digito: "))

print("\n--------------------")
for i in NameFun:
    if (str(i.__name__)) == userFun.lower():
        print("Resultado: " + str(i(primero, segundo)))
print("--------------------")



