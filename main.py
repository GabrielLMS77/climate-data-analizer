import pyodbc 
import requests
import csv

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

print("Connection Successful!")

cursor = connection.cursor()

cursor.execute("SELECT DB_NAME() AS current_database;")

result = cursor.fetchone()
print(result)





