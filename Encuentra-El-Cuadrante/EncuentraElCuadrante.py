#Dos numeros de Entrada 2
while True:
    try: 
        x = float(input("ingresa la coordenada x: "))
        if x == 0:
            print("No se permite que la coordenada sea 0")
        else:
            break
    except ValueError:
        print("Solo puedes usar numeros, no se pueden letras")

while True:
    try: 
        y = float(input("ingresa la coordenada y: "))
        if y == 0:
            print("No se permite que la coordenada sea 0")
        else:
            break
    except ValueError:
        print("Solo puedes usar numeros, no se pueden letras")

#Validaciones de en que cuadrante estan las coordenadas
if x > 0 and y > 0:
    print("Tus coordenadas se encuentran en el Cuad. I")
elif x < 0 and y > 0:
    print("Tus coordenadas se encuentran en el Cuad. II")
elif x < 0 and y < 0:
    print("Tus coordenadas se encuentran en el Cuad. III")
elif x > 0 and y < 0:
    print("Tus coordenadas se encuentran en el Cuad. IV")
else:
    print("")
