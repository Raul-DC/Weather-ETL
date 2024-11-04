# Weather-ETL Project 

## Overview

The **Weather-ETL** project demonstrates an end-to-end ETL (Extract, Transform, Load) process for weather data, providing a practical solution for gathering, processing, and storing weather information. The data flows from a public weather API into a PostgreSQL database and then into Google BigQuery for further analysis and long-term storage.

 OpenWeather 🌦️:

![image](https://github.com/user-attachments/assets/984e639f-0264-449b-b5b0-542ae35862e1)

 PostgreSQL 🐘:

![image](https://github.com/user-attachments/assets/e4741731-f468-4e1f-b68f-3476aa28bef4)

 Google Bigquery 📊🔍:

![image](https://github.com/user-attachments/assets/c8b3a46a-5dfe-4567-a604-e7669315864b)


---

## Key Components 🔑

1. **Data Extraction**⬇️: 
    - Weather data is sourced from the OpenWeather API, which provides real-time information about weather conditions such as temperature, humidity, wind speed, and more.
    - The `extract_transform_load.py` script fetches this data from the API.

2. **Data Loading**⬆️: 
    - The extracted weather data is loaded into a PostgreSQL database, where it is structured and stored.
    - The PostgreSQL database acts as an intermediate storage, facilitating the transformation process.

3. **Data Transformation**♻️: 
    - Raw data obtained from the API undergoes transformation using Python to make it suitable for further analysis.
    - Key fields such as temperature (converted to Celsius), humidity, and wind speed are formatted for consistency.

4. **Data Warehousing**☁️: 
    - Transformed data is uploaded into Google BigQuery for long-term storage and analysis.
    - BigQuery allows for efficient querying and exploration of large datasets.
    - The `from_postgre_to_bigquery.py` script manages this step by extracting data from PostgreSQL and loading it into a pre-configured BigQuery table.

---

## Project Structure 🏢

The repository contains the following structure:

```plaintext
Weather-ETL/
├── sql/
│   ├── Google Bigquery.txt  # SQL script for creating the Google Bigquery table
│   └── PostgreSQL.txt # SQL script for creating the PostgreSQL table
├── scripts/
│   ├── extract_transform_load.py  # Script for data extraction, transformation, and loading into PostgreSQL
│   └── from_postgre_to_bigquery.py # Script for loading data from PostgreSQL to BigQuery
├── .env.example                    # Example of environment variables setup
├── LICENSE
├── README.md                       # This project documentation
└── requirements.txt                # List of dependencies required for the project
```

---

### Scripts 🛠️

1. **extract_transform_load.py**: 
    - This script handles the extraction of weather data from the OpenWeather API, transforming the data into a structured format, and loading it into a PostgreSQL database. It can be executed independently to update the database with the latest weather information.
    - Example of the script output:  
    ![image](https://github.com/user-attachments/assets/7363f686-f68d-43d0-9bcf-b83e58b1d1c7)


2. **from_postgre_to_bigquery.py**: 
    - This script retrieves the transformed data from PostgreSQL and loads it into Google BigQuery for long-term storage. It connects to Google Cloud using service account credentials and automates the process of transferring the weather data into the cloud.
    - Example of the script output:  
    ![image](https://github.com/user-attachments/assets/0ab3603e-d5fc-4248-a680-5530787ae6e2)

---

## How to Set Up 🤔

### Prerequisites ⛔

- **Python 3.x**: Ensure Python is installed.
- **PostgreSQL**: A running PostgreSQL database is required.
- **Google Cloud Account**: To store data in BigQuery, you will need an active Google Cloud account and access to a BigQuery dataset.

### Installation 💾

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/Weather-ETL.git
   cd Weather-ETL
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create your `.env` file in the root directory using the `.env.example` as a template. Fill in the appropriate values for the following variables:
   - `API_KEY`: Your OpenWeather API key.
   - `POSTGRES_URL`: The connection string for your PostgreSQL database.
   - `CREDENTIALS_PATH`: The path to your Google Cloud service account credentials.
   - `TABLE_ID`: The BigQuery table identifier for storing the data.

4. Ensure that your PostgreSQL database has the required table structure by executing the SQL file located in the `sql/` directory:
   
   ```sql
   CREATE TABLE weather_data (
       city STRING,
       country STRING,
       temperature FLOAT,
       weather STRING,
       humidity INTEGER,
       wind_speed FLOAT,
       date_time STRING
   );
   ```

5. Run the ETL process:
   
   - To extract and load data into PostgreSQL:
   
     ```bash
     python scripts/extract_transform_load.py
     ```
   
   - To load data from PostgreSQL to Google BigQuery:
   
     ```bash
     python scripts/from_postgre_to_bigquery.py
     ```
     
---

## How It Works 🔍

1. **API Extraction**: 
   - The project uses the [OpenWeather API](https://openweathermap.org/api) to retrieve real-time weather data for a specific city (La Plata, Argentina in this case).
   - The data is fetched in JSON format, parsed, and cleaned up for the next steps.

2. **Transformation**: 
   - The API provides temperature data in Kelvin, which is converted to Celsius. Similarly, wind speed is measured in meters per second (m/s), and this remains unchanged for accuracy.
   - Additional metadata such as date and time is adjusted to match local time zones (GMT -3).

3. **Data Loading (PostgreSQL)**:
   - The transformed data is loaded into a table called `weather_data`. This relational database allows for structured storage and further processing.
   - Example of table structure:  
     ![image](https://github.com/user-attachments/assets/97040d9f-d92e-4b6c-8179-a48a4a984d9b)

   - Example of a `SELECT *` query:  
     ![image](https://github.com/user-attachments/assets/b994f5cb-8b83-40ea-a7d6-ed116a00d450)


4. **Data Warehousing (Google BigQuery)**:
   - Data is migrated from PostgreSQL to BigQuery, where it can be queried and analyzed at scale using SQL. BigQuery is an ideal tool for storing large volumes of data for analytical purposes.
   - Example of table structure in BigQuery:  
     ![image](https://github.com/user-attachments/assets/0586a499-f970-4716-ad43-36a6a1dc2eef)

   - Example of a `SELECT *` query:  
     ![image](https://github.com/user-attachments/assets/f24e8f89-9030-43f8-b30a-979a61c291f0)

---

## Environment Variables 🌳

The following environment variables are required to run this project:

```plaintext
API_KEY=your_openweather_api_key
CREDENTIALS_PATH=path_to_your_google_cloud_credentials.json
POSTGRES_URL=your_postgresql_connection_string
TABLE_ID=your_bigquery_table_id
```

---

## License ⚖️

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## End 👋🏻

Thank you for taking your time reading this 😃

---
