
num1=20
num2=4

print("Suma: ",(num1 + num2))
print("Resta: ",(num1 - num2))
print("Multiplicacion: ",(num1 * num2))
print("Division Entera: ",(num1 / num2))
print("Division Exacta: ",(num1 // num2))
print("Potencia: ",(num1 ** num2))

#Concatenacion en Python 
texto1 = "Hola"
texto2 = "Mundo"

textoFinal = texto1 + " " + texto2

print(textoFinal)

print("El saludo es: %s %s" % (texto1, texto2))
#En las llaves se coloca el indice de la variable que aparecera en la concatenacion
saludoFinal="Saludo {0} {1}".format(texto1,texto2)

print(saludoFinal)

saludoFinal2 = "Saludo 2: {x} {y}".format(x=texto1,y=texto2)

print(saludoFinal2)