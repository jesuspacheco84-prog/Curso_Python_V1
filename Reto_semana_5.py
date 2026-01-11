# Reto semana 5: calculo de años
entrada = input("Introduce el año actual: ")
año_actual = 0
if entrada.isnumeric():
    año_actual = int(entrada)

entrada_otroaño = input("Introduce otro año para calcular la diferencia: ")

if entrada_otroaño.isnumeric():
    otro_año = int(entrada_otroaño)
    
    if otro_año > año_actual:
        diferencia = otro_año - año_actual
        print(f"Faltan {diferencia} años para llegar al año {otro_año}.")

    elif otro_año < año_actual:
        diferencia = año_actual - otro_año
        print(f"Han pasado {diferencia} años desde el año {otro_año}.")

    else:
        print("Has introducido el mismo año que el actual.")