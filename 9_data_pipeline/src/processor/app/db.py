import mysql.connector # pyright: ignore[reportMissingImports]
import os

def connect_to_db():
    try:
        return mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise

def create_table(cursor):
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS carbon_intensity (
            id INT AUTO_INCREMENT PRIMARY KEY,
            search_date DATE,
            prevision_date DATE,
            intensity_index VARCHAR(255),
            actual INT,
            forecast INT
        )
        """)
    except mysql.connector.Error as e:
        print(f"Erro ao criar tabela: {e}")
        raise

def insert_data(cursor, data):
    for entry in data:
        try:
            cursor.execute("""
            INSERT INTO carbon_intensity (search_date, prevision_date, intensity_index, actual, forecast)
            VALUES (%s, %s, %s, %s, %s)
            """, (entry['search_date'], entry['prevision_date'], entry['index'], entry['actual'], entry['forecast']))
        except mysql.connector.Error as e:
            print(f"Erro ao inserir dados: {e}")