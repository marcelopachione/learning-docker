import sqlite3
import os
import sys

DATABASE = "/app/data/database.db"

# Inicializar DB
def init_db():
    if not os.path.exists("data"):
        os.makedirs("data")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """
    )

    conn.commit()
    conn.close()

    print("Banco de dados disponível...")

# Inserir dado
def data_entry(name):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO entries (name)
            VALUES (?)
    """, (name,)
    )

    conn.commit()
    conn.close()

    print(f"O nome '{name}' foi inserido no banco de dados.")

# Listar dados
def get_entries():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM entries
    """
    )

    entries = cursor.fetchall()
    conn.close()

    print("\nNomes registrados:")
    if entries:
        for entry in entries:
            print(f"ID: {entry[0]} | Nome: {entry[1]}")
    else:
        print("Nenhum nome encontrado.")

# Menu principal
def main():
    # Garante que o banco esteja pronto
    init_db()

    while True:
        print("\nOpções: ")
        print("1. Inserir Nome")
        print("2. Listar Nomes")
        print("3. Sair")

        user_input = input("Insira uma opção [1-3]: ")

        if user_input == "1":
            name = input("Insira um nome para registrar: ")
            data_entry(name)
        elif user_input == "2":
            get_entries()
        elif user_input == "3":
            print("Saindo...")
            sys.exit()
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
