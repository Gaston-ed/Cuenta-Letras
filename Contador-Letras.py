#Contador de letras
#Paso 1 Solicitud de entrada

word = input ("Ingresa la palabra cuyas letras desea contar: ")

#Paso 2 Limpiar espacios y contar las letras
word_clean = word.strip()
cant_letras = len(word_clean)

#Paso 3 Mostrar resultado

print ("La palabra ingresada tinene ",cant_letras," letras.")

