-- SQL query to create the table:

CREATE TABLE `weather_dataset.weather_data` (
    city STRING NULLABLE OPTIONS(description="City name."),
    country STRING NULLABLE OPTIONS(description="Country code (ISO)."),
    temperature FLOAT NULLABLE OPTIONS(description="Temperature in degrees Celsius."),
    weather STRING NULLABLE OPTIONS(description="Climate state."),
    humidity INT64 NULLABLE OPTIONS(description="Percentage of humidity."),
    wind_speed FLOAT NULLABLE OPTIONS(description="Wind speed (m/s)."),
    date_time STRING NULLABLE OPTIONS(description="Date time (GMT -3).")
);
