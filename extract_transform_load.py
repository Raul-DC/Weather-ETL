import requests
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

# Cargar las variables de entorno
load_dotenv()

# Datos de la API
API_KEY = os.getenv('API_KEY')  # Carga la API key desde el archivo .env

# URL de PostgreSQL
POSTGRES_URL = os.getenv('POSTGRES_URL')  # Carga la URL de PostgreSQL desde el archivo .env

# Para la versión 2.5:
CITY = 'La Plata,AR'  # La Plata, Argentina
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

# Para la versión 3.0:
# lat = -34.921263  # Latitud de La Plata
# lon = -57.954351  # Longitud de La Plata
# URL = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}'

# Función para extraer datos de la API
def extract_weather_data():
    print("Extrayendo datos de la API...")
    response = requests.get(URL)
    if response.status_code == 200:
        print("¡Datos obtenidos con éxito!")
        return response.json()
    else:
        print("ERROR al obtener los datos de la API")
        return None

# Función para transformar los datos
def transform_data(data):
    # Extraer información relevante
    # Para la versión 2.5:
    print("Transformando los datos...")
    weather = {
        'city': data['name'],
        'country': data['sys']['country'],  
        'temperature': int(data['main']['temp'] - 273.15),
        'weather': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'date_time': (datetime.utcfromtimestamp(data['dt']) - timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')  # Ajustar a UTC-3
    }
    
    # Para la versión 3.0:
    # weather = {
    #     'latitude': lat,
    #     'longitude': lon,
    #     'temperature': data['current']['temp'],
    #     'weather': data['current']['weather'][0]['description'],
    #     'humidity': data['current']['humidity'],
    #     'wind_speed': data['current']['wind_speed']
    # }

    print("¡Datos transformados con éxito!")
    return pd.DataFrame([weather])

# Función para cargar los datos a PostgreSQL
def load_data(df):
    print("Cargando los datos a PostgreSQL...")
    # Configuración de la base de datos PostgreSQL
    engine = create_engine(POSTGRES_URL)

    # Cargando los datos a una tabla llamada "weather_data" (la tabla se crea desde 0 sino existe)
    df.to_sql('weather_data', engine, if_exists='replace', index=False)
    print("¡Datos cargados exitosamente en PostgreSQL! (Fin de la ejecucíon)")

# Proceso ETL (app.py)
def etl_process():
    data = extract_weather_data()
    if data:
        df = transform_data(data)
        load_data(df);
    else:
        print("No se pudo conseguir la Data");

if __name__ == "__main__":
    etl_process()
