import random
import matplotlib.pyplot as plt

# Función 1: Calcular los resultados de las canicas
def simular_galton(canicas=3000, niveles=12):
    """
    Simula el paso de las canicas por los niveles de obstáculos.
    """
    contenedores = []
    
    for _ in range(canicas):
        pasos_derecha = 0
        for _ in range(niveles):
            # Decidir aleatoriamente: 1 es derecha, 0 es izquierda
            pasos_derecha += random.randint(0, 1)
        
        contenedores.append(pasos_derecha)
    
    return contenedores

# Función 2: Graficación del histograma
def graficar_resultados(resultados):
    """
    Crea un histograma con los resultados de la simulación.
    """
    plt.figure(figsize=(10, 6))
    
    # Crear el histograma (bins 13 para cubrir de 0 a 12 contenedores)
    plt.hist(resultados, bins=range(14), align='left', rwidth=0.8, color='steelblue')
    
    # Configuración de etiquetas y título (Requisito de la rúbrica)
    plt.title("Simulación de la Máquina de Galton", fontsize=14)
    plt.xlabel("Distribución de canicas", fontsize=12)
    plt.ylabel("Cantidad de canicas", fontsize=12)
    
    plt.grid(axis='y', alpha=0.75)
    plt.show()

if __name__ == "__main__":
    total_canicas = 3000
    niveles_obstaculos = 12
    
    print(f"Iniciando simulación de {total_canicas} canicas...")
    
    # Obtener datos
    datos_contenedores = simular_galton(total_canicas, niveles_obstaculos)
    
    # Generar gráfica
    graficar_resultados(datos_contenedores)
    print("Simulación completada con éxito.")