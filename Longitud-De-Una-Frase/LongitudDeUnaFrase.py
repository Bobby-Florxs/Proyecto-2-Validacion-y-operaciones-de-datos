frase = input("ingresa la palabra clave: ")
longitud = len(frase)
ls= 8 #limite superior
li= 4 #limite inferior 
if ls > longitud and li<longitud: 
    print("La palabra es correcta")
elif longitud < li :
    print(f"Hacen falta letras. Solo tiene {longitud} letras")
elif longitud > ls:
    print(f"Sobran letras. Tiene {longitud} letras")
else:
    print("")