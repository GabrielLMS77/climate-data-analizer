import csv
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

print("Connection Successfull!")

with open("weather_data.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    rows = []

    for row in reader:
        rows.append((
            row["date"],
            row["temperature_max"],
            row["temperature_min"],
            row["precipitation"]
        ))

print("Number of rows:", len(rows))
print("First row:", rows[0] if rows else "No data found")

if rows:
   sql = """
IF NOT EXISTS (
    SELECT 1
    FROM dbo.WeatherObservations
    WHERE observation_date = ?
)
BEGIN
    INSERT INTO dbo.WeatherObservations
        (observation_date, temperature_max, temperature_min, precipitation)
    VALUES (?, ?, ?, ?)
END
"""

cursor = connection.cursor()

cursor.execute("""
    SELECT
        DB_NAME() AS current_database,
        OBJECT_ID('dbo.WeatherObservations', 'U') AS table_id
""")

print("Database and table check:", cursor.fetchone())

parameters = [
    (row[0], row[0], row[1], row[2], row[3])
    for row in rows
]

cursor.executemany(sql, parameters)
connection.commit()


print(len(rows), "records inserted successfully!")

cursor.close()
connection.close()
    
