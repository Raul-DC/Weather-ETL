-- SQL query to create the table:

CREATE TABLE weather_data (
    country TEXT,
    city TEXT,
    weather TEXT,
    temperature BIGINT,
    humidity BIGINT,
    wind_speed DOUBLE PRECISION,
    date_time TIMESTAMP WITH TIME ZONE
);
