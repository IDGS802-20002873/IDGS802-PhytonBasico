
print("Suma de numeros")

num1 = int(input('Dame num 1: '))
num2 = int(input('Dame num 2: '))

if num1>num2:
    print("El {} es mayor que el {}".format(num1, num2,))
else:
    print("El {} es mayor que el {}".format(num1, num2,))

print("------------------Pedir una edad------------------")
edad = int(input("Ingresa una edad: "))
if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes 18")
else:
    print("No eres mayor de edad")