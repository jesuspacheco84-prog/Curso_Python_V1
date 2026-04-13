import requests # Librería necesaria para hacer peticiones a internet

# --- PROGRAMA DE CONSULTA DE CLIMA (SEMANA 15) ---
# Este programa conecta con la API de OpenWeather para obtener datos reales.

def obtener_clima():
    # Bloque: Configuración de la petición
    api_key = "9b26bf56bc321cb85843b1055ad3420a" 
    latitud = "19.551942" #Ejemplo: Tlalnepantla, México
    longitud = "-99.192585" #Ejemplo: Tlalnepantla, México
    
    # Bloque: Construcción de la URL (Petición GET)
    # Usamos unidades métricas para grados Celsius
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={api_key}&units=metric&lang=es"

    try:
        # Bloque: Ejecución de la petición a la API
        print("Consultando el clima actual...")
        respuesta = requests.get(url)
        
        # Bloque: Procesamiento de la respuesta
        # Si la respuesta es exitosa (código 200), extraemos los datos
        if respuesta.status_code == 200:
            datos = respuesta.json()
            
            ciudad = datos["name"]
            temp = datos["main"]["temp"]
            descripcion = datos["weather"][0]["description"]
            humedad = datos["main"]["humidity"]

            # Bloque: Visualización de resultados
            print("\n" + "="*30)
            print(f"🌍 CLIMA EN: {ciudad}")
            print(f"🌡️ Temperatura: {temp}°C")
            print(f"☁️ Estado: {descripcion.capitalize()}")
            print(f"💧 Humedad: {humedad}%")
            print("="*30)
        else:
            print(f"Error en la petición. Código: {respuesta.status_code}")
            print("Verifica que tu API Key sea correcta y esté activa.")

    except Exception as e:
        print(f"Ocurrió un error al conectar con el servidor: {e}")

if __name__ == "__main__":
    obtener_clima()