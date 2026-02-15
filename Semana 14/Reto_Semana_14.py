import os

# --- PROGRAMA DE EDICIÓN DE CONTACTOS CON CONFIRMACIÓN (SEMANA 14) ---
# Este programa permite ver qué datos se cambiaron exactamente.

def gestionar_contactos():
    # Bloque: Localización del archivo
    carpeta_actual = os.path.dirname(__file__)
    archivo_nombre = os.path.join(carpeta_actual, "contactos.txt")

    try:
        # Bloque: Lectura del archivo
        with open(archivo_nombre, "r") as archivo:
            lineas = archivo.readlines()
        
        if not lineas:
            print("El archivo está vacío.")
            return

        # Bloque: Mostrar contactos numerados
        print("\n--- LISTA DE CONTACTOS ---")
        for i, linea in enumerate(lineas, 1):
            print(f"{i}. {linea.strip()}")

        # Bloque: Selección del contacto
        while True:
            try:
                seleccion = int(input("\n¿Qué número de contacto quieres editar?: "))
                if 1 <= seleccion <= len(lineas):
                    indice = seleccion - 1
                    break
                else:
                    print(f"Error: Elige entre 1 y {len(lineas)}.")
            except ValueError:
                print("Error: Ingresa un número entero.")

        # Bloque: Captura de nuevos datos
        print(f"\nEditando contacto #{seleccion}...")
        nombre = input("Nuevo nombre: ").strip()
        tel = input("Nuevo teléfono: ").strip()
        correo = input("Nuevo correo: ").strip()

        # Bloque: Preparación del nuevo dato y actualización
        # Guardamos la nueva línea en una variable para mostrarla al final
        nueva_informacion = f"{nombre}, {tel}, {correo}"
        lineas[indice] = nueva_informacion + "\n"

        # Bloque: Escritura en el archivo
        with open(archivo_nombre, "w") as archivo:
            archivo.writelines(lineas)
        
        # Bloque: Confirmación detallada
        # Aquí mostramos exactamente qué se guardó
        print("\n" + "="*40)
        print("✔ ¡ACTUALIZACIÓN EXITOSA!")
        print(f"Dato guardado: {nueva_informacion}")
        print("="*40)

    except FileNotFoundError:
        print(f"Error: No se encontró 'contactos.txt' en la carpeta.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    gestionar_contactos()