import pyodbc

server = r"localhost\SQLEXPRESS"
database = "ClimateData"

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

connection = pyodbc.connect(connection_string)
cursor = connection.cursor()


sql = """
SELECT
    COUNT(*) AS total_days,
    AVG(temperature_max) AS average_max_temperature,
    MIN(temperature_min) AS lowest_temperature,
    MAX(precipitation) AS highest_precipitation
FROM dbo.WeatherObservations;
"""

cursor.execute(sql)
result = cursor.fetchone()

print("Total of records:", result[0])
print("Average maximum temperature:", result[1])
print("Lowest minimum temperature:", result[2])
print("Highest precipitation:", result[3])

cursor.close()
connection.close()