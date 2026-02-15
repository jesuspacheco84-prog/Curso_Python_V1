# Reto semana 10: Manipulación de Listas y Funciones
# Objetivo: Crear dos listas y filtrar elementos comunes.

def crear_lista(nombre_de_la_lista):
    """
    Crea una lista con longitud y elementos definidos por el usuario.
    Incluye validación para asegurar que la longitud sea un número.
    """
    lista = []
    while True:
        try:
            longitud = int(input(f"\n¿Cuántos elementos tendrá la {nombre_de_la_lista}? "))
            if longitud < 0:
                print("Por favor, ingresa un número positivo.")
                continue
            break
        except ValueError:
            print("Error: Debes ingresar un número entero para la longitud.")

    for i in range(longitud):
        elemento = input(f"  -> Introduce el elemento {i+1} de la {nombre_de_la_lista}: ").strip()
        lista.append(elemento)
    return lista

def eliminar_duplicados_externos(base, filtro):
    """
    Retorna una nueva lista con los elementos de 'base' 
    que no se encuentran en 'filtro'.
    """
    # Usamos set para que la búsqueda sea mucho más rápida
    set_filtro = set(filtro)
    return [item for item in base if item not in set_filtro]

# --- Ejecución del Programa ---

# 1. Creación de listas
lista_a = crear_lista("Primera Lista")
lista_b = crear_lista("Segunda Lista")

# 2. Impresión de listas originales
print("\n" + "="*30)
print("LISTAS ORIGINALES")
print(f"Lista 1: {lista_a}")
print(f"Lista 2: {lista_b}")
print("="*30)

# 3. Proceso de eliminación
lista_final = eliminar_duplicados_externos(lista_a, lista_b)

# 4. Resultado final
print("\nRESULTADO FINAL")
print(f"Lista 1 actualizada (sin elementos de la Lista 2): {lista_final}")
print("="*30)