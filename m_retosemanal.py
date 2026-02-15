# m_retosemanal.py

def crear_varias_listas():
    lista_de_listas = []
    try:
        cantidad_listas = int(input("¿Cuántas listas deseas crear? "))
        for i in range(cantidad_listas):
            print(f"\n--- Configurando Lista {i+1} ---")
            longitud = int(input(f"¿Cuántos elementos tendrá la lista {i+1}? "))
            nueva_lista = []
            for j in range(longitud):
                item = input(f"  Introduce el elemento {j+1}: ")
                nueva_lista.append(item)
            lista_de_listas.append(nueva_lista)
        return lista_de_listas
    except ValueError:
        print("Error: Ingresa números enteros.")
        return []

def filtrar_listas_posteriores(listas):
    listas_limpias = []
    for i in range(len(listas)):
        lista_actual = listas[i]
        elementos_posteriores = []
        for lista_posterior in listas[i+1:]:
            elementos_posteriores.extend(lista_posterior)
        set_posteriores = set(elementos_posteriores)
        nueva_lista = [item for item in lista_actual if item not in set_posteriores]
        listas_limpias.append(nueva_lista)
    return listas_limpias