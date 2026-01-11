# NOMBRE_APELLIDO_proyectoM2.py
# Proyecto: Validación y operaciones de datos

'''
RETO 1: Longitud de una frase
El programa identifica si una palabra tiene entre 4 y 8 letras.
'''

print("--- 1. Longitud de una frase ---")
palabra = input("Por favor, ingresa una palabra: ")
longitud = len(palabra)

# Verificamos si la longitud está en el rango correcto (4 a 8 letras) [cite: 18]
if 4 <= longitud <= 8:
    print("La palabra es correcta.")
# Si tiene menos de 4 letras [cite: 19]
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
# Si tiene más de 8 letras [cite: 20]
else:
    print(f"Sobran letras. Tiene {longitud} letras.")


print("\n" + "-"*30 + "\n")


'''
RETO 2: Encuentra el cuadrante
El programa identifica en qué cuadrante del plano cartesiano se encuentra un punto (X, Y).
'''

print("--- 2. Encuentra el cuadrante ---")

# Solicitamos las coordenadas X y Y
x = float(input("Ingrese X: "))
y = float(input("Ingrese Y: "))

# Verificamos que ninguna coordenada sea 0 [cite: 86]
if x == 0 or y == 0:
    print("Error: Las coordenadas no pueden ser 0.")
else:
    # Lógica para identificar los cuadrantes según los signos (+ o -) [cite: 90]
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV")

print("\nPrograma finalizado.")