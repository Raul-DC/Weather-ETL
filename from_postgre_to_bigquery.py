from google.cloud import bigquery
from sqlalchemy import create_engine
import pandas as pd
import os
from google.oauth2 import service_account

# Ruta al archivo de credenciales
CREDENTIALS_PATH = 'C:/Users/User/Desktop/RHLoop notes/Proyectos/Proyecto 1 - PostgreSQL/script/clave Bigquery/weather-project-439111-e7a7246cd754.json'

# Autenticación utilizando el archivo de credenciales
credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH)

# Función para extraer los datos de PostgreSQL
def extract_data_from_postgres():
    try:
        print('Extrayendo datos de PostgreSQL...')
        engine = create_engine('postgresql://postgres:123456789@localhost:5000/weather_db')
        query = "SELECT * FROM weather_data"
        df = pd.read_sql(query, engine)
        if df.empty:
            print('Advertencia: No se encontraron datos en la tabla weather_data de PostgreSQL.')
            return None
        else:
            print('¡Datos extraidos con éxito!')
            return df
    except Exception as e:
        print(f"Error al extraer datos de PostgreSQL: {e}")
        return None

# Función para cargar los datos a BigQuery
def load_data_to_bigquery(df):
    try:
        if df is None or df.empty:
            print('No hay datos para cargar en BigQuery.')
            return None
        else:
            print('Iniciando carga de datos a Google Bigquery...')
            client = bigquery.Client(credentials=credentials)  # Usa las credenciales al crear el cliente
            table_id = "weather-project-439111.weather_dataset.weather_data" # Google Cloud -> Project ID.Dataset Name.Table Name
        
            job = client.load_table_from_dataframe(df, table_id)
            job.result()  # Esperar a que el job termine
            print("¡Datos cargados exitosamente en BigQuery!")
    except Exception as e:
        print(f"Error al cargar datos en BigQuery: {e}")

# Proceso ETL a BigQuery (app.py)
def etl_to_bigquery():
    df = extract_data_from_postgres()
    load_data_to_bigquery(df)

if __name__ == "__main__":
    etl_to_bigquery()