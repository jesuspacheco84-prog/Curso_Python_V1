#Obtenemos la cantidad de personas
personas = int(input( 'personas: '))

#Verificamos que la cantidad sea mayor a 0 si no, no tiene sentido pedir nada
while personas > 0:
    #Pedimos el nomrbre de la persona
    nombre = input('Introduca su nombre completo por favor: ')
    #Pedimos su edad
    e = int(input('Introduzca su edad en años por favor: '))
    #Pedimos su estatura
    est = float(input('Introduzca su estatura en metros por favor: '))
    #Pedimos su peso
    p = float(input('Introduzca su peso en kg por favor: '))
    #Calculamos el IMC  
    IMC = p / (est * est)   

    #Le decimos si es menor o mayor de edad, si es menor a 18 es menor, si no es mayor edad
    #Solo ruegue porque a nadie se le ocurra meter numeros negativos, le va a decir que es menor de edad

    if(e <18):
        print("Usted es menor de edad")

    else:
        print("Usted es mayor de edad")

    #Le imprimos el IMC para que se ponga sad
    print("IMC: " + str(IMC) )

    #Hacemos las distintas validaciones
    if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
    elif IMC >= 40.00:
        print ("obesidad morbida")

    #Por cada persona a la que le pedimos los datos debemos restarle una (Porque ya la recorrimos)
    #si no el ciclo se vuelve infinito
    personas = personas - 1