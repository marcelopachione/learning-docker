import json
import os
from datetime import date
from config import OUTPUT_DIR

def save_data_to_file(data):
    today = date.today()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_path = os.path.join(OUTPUT_DIR, today.strftime('%Y-%m-%d') + ".json")
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Arquivo salvo em {file_path}")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")