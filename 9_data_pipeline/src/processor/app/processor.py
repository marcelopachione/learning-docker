from datetime import date
from loader import load_data
from db import connect_to_db, create_table, insert_data

def main():
    today = date.today()
    file_path = f"/data/{today.strftime('%Y-%m-%d')}.json"
    data = load_data(file_path)
    if not data:
        print("Nenhum dado para processar.")
        return

    try:
        db = connect_to_db()
        cursor = db.cursor()
        create_table(cursor)
        insert_data(cursor, data)
        db.commit()
    except Exception as e:
        print(f"Erro no processamento: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

if __name__ == "__main__":
    main()