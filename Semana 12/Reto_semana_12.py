import matplotlib.pyplot as plt

def programa_ventas():
    print("=== GRAFICADOR DE VENTAS ANUALES ===")
    
    try:
        # 1. Pedir el rango de años
        inicio = int(input("Introduce el año inicial (ej. 2015): "))
        fin = int(input("Introduce el año final (ej. 2022): "))
        
        if inicio > fin:
            print("Error: El año inicial debe ser menor al final.")
            return

        años = []
        ventas = []

        # 2. Pedir las ventas de cada año
        print(f"\nPor favor, introduce las ventas para el periodo {inicio}-{fin}:")
        for año in range(inicio, fin + 1):
            v = float(input(f"Ventas del año {año}: "))
            años.append(año)
            ventas.append(v)

        # 3. Crear la gráfica
        plt.figure(figsize=(10, 6)) # Tamaño de la ventana
        plt.plot(años, ventas, marker='o', color='blue', linewidth=2, label='Ventas')
        
        # Personalización (como en el PDF)
        plt.title(f"Ventas del {inicio} al {fin}", fontsize=14)
        plt.xlabel("Año", fontsize=12)
        plt.ylabel("Ventas", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7) # Cuadrícula punteada
        plt.legend()

        # 4. Mostrar el resultado
        print("\n¡Gráfica generada! Revisa la ventana emergente.")
        plt.show()

    except ValueError:
        print("Error: Ingresa solo números válidos para años y ventas.")

if __name__ == "__main__":
    programa_ventas()