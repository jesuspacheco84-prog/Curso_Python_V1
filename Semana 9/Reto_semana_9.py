# Actividad RETO 9: Funciones y Manipulación de Caracteres
# Objetivo: Identificar letras adyacentes en el alfabeto.

def obtener_adyacentes(letra):
    """
    Función que calcula la letra anterior y siguiente.
    Utiliza el código ASCII para mayor eficiencia.
    """
    # Verificamos que sea una sola letra y que sea del alfabeto
    if len(letra) == 1 and letra.isalpha():
        # ord() convierte la letra a su número en la tabla ASCII
        codigo = ord(letra)
        
        # Manejo de la letra anterior (a = 97 en ASCII)
        anterior = chr(codigo - 1) if letra != 'a' else "No existe (es la primera)"
        
        # Manejo de la letra siguiente (z = 122 en ASCII)
        siguiente = chr(codigo + 1) if letra != 'z' else "No existe (es la última)"
        
        return anterior, siguiente
    return None

# --- Bucle Principal ---
print("--- Buscador de Letras Adyacentes ---")

while True:
    # Solicitamos la entrada y limpiamos espacios en blanco
    entrada = input("\nIngrese una letra (Presione ENTER para salir): ").lower().strip()
    
    # Condición de salida: si la cadena está vacía
    if not entrada:
        print("Saliendo del programa... ¡Hasta luego!")
        break
    
    # Llamada a la función
    resultado = obtener_adyacentes(entrada)
    
    if resultado:
        ant, sig = resultado
        print(f"Letra ingresada: {entrada}")
        print(f"  - Anterior:  {ant}")
        print(f"  - Siguiente: {sig}")
    else:
        print("Error: Por favor, ingrese un solo carácter válido (A-Z).")