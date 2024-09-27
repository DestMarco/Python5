
import json
import jsonschema
import requests
import sys



def SerializaJson(dData, file_path) -> bool:

    try:
        # Scrive il dizionario in un file JSON
        with open(file_path, 'w') as file:
            json.dump(dData, file, indent=4)
        return True
    except Exception as e:
        print(f"Errore durante la serializzazione: {e}")
        return False

def DeserializeJson(file_path) -> dict:

    try:
        # Legge e converte il contenuto JSON in un dizionario
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Errore durante la deserializzazione: {e}")
        return {}

