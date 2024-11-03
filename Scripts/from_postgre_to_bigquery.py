from google.cloud import bigquery
from sqlalchemy import create_engine
import pandas as pd
import os
from google.oauth2 import service_account
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Path to the credentials file
CREDENTIALS_PATH = os.getenv('CREDENTIALS_PATH')

# Authentication using the credentials file
credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH)

# Function to extract data from PostgreSQL
def extract_data_from_postgres():
    try:
        print('Extracting data from PostgreSQL...')
        POSTGRES_URL = os.getenv('POSTGRES_URL')
        engine = create_engine(POSTGRES_URL)
        query = "SELECT * FROM weather_data"
        df = pd.read_sql(query, engine)
        if df.empty:
            print('Warning: No data found in the weather_data table in PostgreSQL.')
            return None
        else:
            print('Data extracted successfully!')
            return df
    except Exception as e:
        print(f"Error extracting data from PostgreSQL: {e}")
        return None

# Function to load data to BigQuery
def load_data_to_bigquery(df):
    try:
        if df is None or df.empty:
            print('No data to load into BigQuery.')
            return None
        else:
            print('Starting data load to Google BigQuery...')
            client = bigquery.Client(credentials=credentials)  # Use the credentials when creating the client
            table_id = os.getenv('TABLE_ID')  # Google Cloud -> [Project ID].[Dataset Name].[Table Name]
        
            job = client.load_table_from_dataframe(df, table_id)
            job.result()  # Wait for the job to finish
            print("Data loaded successfully into BigQuery!")
    except Exception as e:
        print(f"Error loading data into BigQuery: {e}")

# ETL process to BigQuery (app.py)
def etl_to_bigquery():
    df = extract_data_from_postgres()
    load_data_to_bigquery(df)

if __name__ == "__main__":
    etl_to_bigquery()