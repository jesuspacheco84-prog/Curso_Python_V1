# main.py
import m_retosemanal as modulo

# 1. Crear listas
listas_originales = modulo.crear_varias_listas()

# 2. Imprimir originales
print("\nLISTAS ORIGINALES:")
for i, l in enumerate(listas_originales):
    print(f"Lista {i+1}: {l}")

# 3. Procesar
listas_finales = modulo.filtrar_listas_posteriores(listas_originales)

# 4. Imprimir resultados
print("\nLISTAS ACTUALIZADAS (Sin elementos de posteriores):")
for i, l in enumerate(listas_finales):
    print(f"Lista {i+1}: {l}")