# Climate Data Analyzer

A Python and SQL Server project that collects, stores, and analyzes daily weather data using the Open-Meteo API.

## Project Overview

This project demonstrates a simple data pipeline, from API data collection to database storage and SQL-based analysis.

The pipeline includes:
1. Fetching weather data from the Open-Meteo API.
2. Exporting the collected data to a CSV file.
3. Loading weather observations into a SQL Server database.
4. Analyzing temperature and precipitation data using SQL and Python.
5. Preventing duplicate daily observations in the database.

## Technologies

- Python
- Requests
- CSV
- pyodbc
- Microsoft SQL Server
- SQL
- Open-Meteo API
- Git and GitHub

## Project Structure

```text
climate-data-analyzer/
├── fetch_weather.py
├── load_weather.py
├── analyze_weather.py
├── weather_data.csv
└── README.md
```

## Data Collected

The dataset includes:
- Observation date
- Maximum daily temperature
- Minimum daily temperature
- Daily precipitation

The current dataset contains a small number of daily observations for testing and learning purposes.

## Database

The project uses a SQL Server database named `ClimateData` and a table named `dbo.WeatherObservations`.

A unique constraint on the observation date helps prevent duplicate daily records.

## How to Run

1. Install Python and Microsoft SQL Server.
2. Install the required Python packages:

   ```bash
   python -m pip install requests pyodbc
   ```

3. Configure the SQL Server connection in the Python scripts to match your local environment.
4. Run the weather collection script:

   ```bash
   python fetch_weather.py
   ```

5. Run the data loading script:

   ```bash
   python load_weather.py
   ```

6. Run the analysis script:

   ```bash
   python analyze_weather.py
   ```

Make sure the SQL Server database and table have been created before loading the data.

## Learning Goals

This project was built to practice:
- Python fundamentals
- Working with REST APIs
- Reading and writing CSV files
- Connecting Python to SQL Server
- Writing SQL queries and aggregations
- Data quality and duplicate prevention
- Version control with Git and GitHub

## Future Improvements

- Add automated data updates.
- Support multiple cities.
- Improve error handling and logging.
- Add weather data visualizations.
- Automate the entire pipeline.

## Data Source

Weather data is provided by the [Open-Meteo API](https://open-meteo.com/).
