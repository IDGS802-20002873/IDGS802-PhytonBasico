
texto = " Universidad Tecnologica de Leon"

print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title())
#Encuentra la posicion del valor
print(texto.find("de"))
#Numero de apariciones en la cadena
print(texto.count("e"))

textoNuevo = texto.replace("e","3")
print(textoNuevo)