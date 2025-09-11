import json

def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return []