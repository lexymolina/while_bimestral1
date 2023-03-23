#ejemplo 2
num = int(input("escribe un numero positivo: "))
while num < 0:
    print("este es un numero negativo, prueba de nuevo")
    num = int(input("escribe un numero positivo: "))
print("el numero es: " ,num)