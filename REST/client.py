import json
import requests

base_url = "http://127.0.0.1:8080"

def RichiedidatiCittadino():
    nome = input("inserisci nome cittadino: ")
    cognome = input("inserisci cognome cittadino: ")
    dataNascita = input("inserisci data cittadino: ")
    codiceFiscale = input("inserisci codice fiscale cittadino: ")
    jReqiuest = {
        "nome": nome,
        "cognome": cognome,
        "datanascita": dataNascita,
        "codicefiscale": codiceFiscale
    }
    return jReqiuest

def CreaInterfaccia():
    print("Operazioni disponibili:")
    print("1. Inserisci cittadino (es. atto di nascita)")
    print("2. Richiedi dati di accesso (es. cert. residenza)")
    print("3. Modifica dati cittadino")
    print("4. Elimina cittadino")
    print("5. Exit")

def ModificaDatiCittadino():
    codiceFiscale = input("Inserisci codice fiscale del cittadino da modificare: ")
    print("Inserisci i nuovi dati del cittadino:")
    jsonDataRequest = RichiedidatiCittadino()
    jsonDataRequest["codicefiscale"] = codiceFiscale  # Mantiene il codice fiscale invariato
    return jsonDataRequest

def EliminaCittadino():
    codiceFiscale = input("Inserisci codice fiscale del cittadino da eliminare: ")
    return {"codicefiscale": codiceFiscale}

CreaInterfaccia()
sOper = input("Seleziona operazione: ")

while sOper != "5":
    if sOper == "1":
        print("Richiesta per aggiungere cittadino")
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = RichiedidatiCittadino()
        try:
            response = requests.post(api_url, json=jsonDataRequest)
            print(response.status_code)
            print(response.json())
        except Exception as e:
            print("Problemi di comunicazione:", str(e))

    elif sOper == "3":
        print("Modifica dati cittadino")
        api_url = base_url + "/update_cittadino"
        jsonDataRequest = ModificaDatiCittadino()
        try:
            response = requests.put(api_url, json=jsonDataRequest)
            print(response.status_code)
            print(response.json())
        except Exception as e:
            print("Problemi di comunicazione:", str(e))

    elif sOper == "4":
        print("Elimina cittadino")
        api_url = base_url + "/delete_cittadino"
        jsonDataRequest = EliminaCittadino()
        try:
            response = requests.delete(api_url, json=jsonDataRequest)
            print(response.status_code)
            print(response.json())
        except Exception as e:
            print("Problemi di comunicazione:", str(e))

    CreaInterfaccia()
    sOper = input("Seleziona operazione: ")

