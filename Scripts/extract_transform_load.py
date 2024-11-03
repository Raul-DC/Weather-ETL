import requests
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

# API data
API_KEY = os.getenv('API_KEY')  # Load the API key from the .env file

# PostgreSQL URL
POSTGRES_URL = os.getenv('POSTGRES_URL')  # Load the PostgreSQL URL from the .env file

# For version 2.5:
CITY = 'La Plata,AR'  # La Plata, Argentina
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

# For version 3.0:
# lat = -34.921263  # Latitude of La Plata
# lon = -57.954351  # Longitude of La Plata
# URL = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}'

# Function to extract data from the API
def extract_weather_data():
    print("Extracting data from the API...")
    response = requests.get(URL)
    if response.status_code == 200:
        print("Data obtained successfully!")
        return response.json()
    else:
        print("ERROR obtaining data from the API")
        return None

# Function to transform the data
def transform_data(data):
    # Extract relevant information
    # For version 2.5:
    print("Transforming the data...")
    weather = {
        'city': data['name'],
        'country': data['sys']['country'],  
        'temperature': int(data['main']['temp'] - 273.15),
        'weather': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'date_time': (datetime.utcfromtimestamp(data['dt']) - timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')  # Adjust to UTC-3
    }
    
    # For version 3.0:
    # weather = {
    #     'latitude': lat,
    #     'longitude': lon,
    #     'temperature': data['current']['temp'],
    #     'weather': data['current']['weather'][0]['description'],
    #     'humidity': data['current']['humidity'],
    #     'wind_speed': data['current']['wind_speed']
    # }

    print("Data transformed successfully!")
    return pd.DataFrame([weather])

# Function to load the data into PostgreSQL
def load_data(df):
    print("Loading data into PostgreSQL...")
    # PostgreSQL database configuration
    engine = create_engine(POSTGRES_URL)

    # Loading data into a table called "weather_data" (the table is created from scratch if it does not exist)
    df.to_sql('weather_data', engine, if_exists='replace', index=False)
    print("Data loaded successfully into PostgreSQL!")

# ETL process (app.py)
def etl_process():
    data = extract_weather_data()
    if data:
        df = transform_data(data)
        load_data(df)
    else:
        print("Could not obtain the data.")

if __name__ == "__main__":
    etl_process()