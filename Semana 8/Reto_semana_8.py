# Reto semana 8: Colores en dos idiomas (Inglés y Francés)

diccionario_colores_ingles = {
    "rojo": "red", "naranja": "orange", "amarillo": "yellow",
    "verde": "green", "azul": "blue", "violeta": "purple", "añil": "indigo"
}

diccionario_colores_frances = {
    "verde": "vert", "azul": "bleu", "violeta": "violet", "rojo": "rouge",
    "naranja": "orange", "amarillo": "jaune", "añil": "indigo"
}

print("¡Bienvenido! Puedes traducir colores del arcoíris a: inglés o francés.")

# Elección de idioma con validación (soporta tildes)
while True:
    idioma_input = input("Selecciona 'ingles' o 'frances': ").lower().strip()
    
    if idioma_input in ["ingles", "inglés"]:
        idioma = "ingles"
        dict_colores = diccionario_colores_ingles
        prompt = "Select a color from the rainbow (ej: el cielo es azul): "
        break
    elif idioma_input in ["frances", "francés"]:
        idioma = "frances"
        dict_colores = diccionario_colores_frances
        prompt = "Choisis une couleur de l'arc-en-ciel (ej: la pomme est roja): "
        break
    else:
        print("Opción inválida. Intenta de nuevo.")

# Bucle principal para oraciones
while True:
    oracion = input(prompt).lower()
    color_encontrado = None
    
    # Buscamos si alguna de las llaves del diccionario está en la oración
    for color_es in dict_colores:
        if color_es in oracion:
            color_encontrado = color_es
            break
    
    if color_encontrado:
        traduccion = dict_colores[color_encontrado]
        print(f"'{color_encontrado}' se dice '{traduccion}' en {idioma}.")
    else:
        print("No se encontró un color del arcoíris en tu oración.")
    
    # Opción para salir o continuar
    continuar = input("¿Deseas traducir otro color? (s/n): ").lower().strip()
    if continuar != 's':
        print("¡Hasta luego! Gracias por usar el traductor.")
        break