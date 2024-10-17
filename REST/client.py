import json
import requests

base_url = "http://127.0.0.1:8080"

# Funzione per richiedere nome utente e password
def Autenticazione():
    nome_utente = input("Inserisci il nome utente: ")
    password = input("Inserisci la password: ")
    return {"nome_utente": nome_utente, "password": password}

# Funzione per richiedere i dati del cittadino
def RichiedidatiCittadino():
    nome = input("Inserisci nome cittadino: ")
    cognome = input("Inserisci cognome cittadino: ")
    dataNascita = input("Inserisci data di nascita (YYYY-MM-DD): ")
    codiceFiscale = input("Inserisci codice fiscale cittadino: ")
    jRequest = {
        "nome": nome,
        "cognome": cognome,
        "datanascita": dataNascita,
        "codicefiscale": codiceFiscale
    }
    return jRequest

# Funzione per creare l'interfaccia delle operazioni
def CreaInterfaccia():
    print("Operazioni disponibili:")
    print("1. Inserisci cittadino (es. atto di nascita)")
    print("2. Richiedi dati di accesso (es. cert. residenza)")
    print("3. Modifica dati cittadino")
    print("4. Elimina cittadino")
    print("5. Exit")

# Funzione per modificare i dati di un cittadino
def ModificaDatiCittadino():
    codiceFiscale = input("Inserisci codice fiscale del cittadino da modificare: ")
    print("Inserisci i nuovi dati del cittadino:")
    jsonDataRequest = RichiedidatiCittadino()
    jsonDataRequest["codicefiscale"] = codiceFiscale  # Mantiene il codice fiscale invariato
    return jsonDataRequest

# Funzione per eliminare un cittadino
def EliminaCittadino():
    codiceFiscale = input("Inserisci codice fiscale del cittadino da eliminare: ")
    return {"codicefiscale": codiceFiscale}

# Inizio del client
autenticazione = Autenticazione()

# Verifica delle credenziali
api_url = base_url + "/login"
try:
    response = requests.post(api_url, json=autenticazione)
    if response.status_code == 200:
        print("Autenticazione riuscita!")
    else:
        print("Autenticazione fallita!")
        exit()
except Exception as e:
    print("Problemi di comunicazione:", str(e))
    exit()

# Mostra il menu solo dopo l'autenticazione riuscita
CreaInterfaccia()
sOper = input("Seleziona operazione: ")

while sOper != "5":
    if sOper == "1":
        print("Richiesta per aggiungere cittadino")
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = RichiedidatiCittadino()
        try:
            response = requests.post(api_url, json=jsonDataRequest, headers=autenticazione)
            print(response.status_code)
            print(response.json())
        except Exception as e:
            print("Problemi di comunicazione:", str(e))

    elif sOper == "2":
        codiceFiscale = input("Inserisci il codice fiscale del cittadino: ")
        api_url = base_url + f"/get_cittadino/{codiceFiscale}"
        try:
            response = requests.get(api_url, headers=autenticazione)
            print(response.status_code)
            print(response.json())
        except Exception as e:
            print("Problemi di comunicazione:", str(e))

    elif sOper == "3":
        print("Modifica dati cittadino")
        api_url = base_url + "/update_cittadino"
        jsonDataRequest = ModificaDatiCittadino()
        try:
            response = requests.put(api_url, json=jsonDataRequest, headers=autenticazione)
            print(response.status_code)
            print(response.json())
        except Exception as e:
            print("Problemi di comunicazione:", str(e))

    elif sOper == "4":
        print("Elimina cittadino")
        api_url = base_url + "/delete_cittadino"
        jsonDataRequest = EliminaCittadino()
        try:
            response = requests.delete(api_url, json=jsonDataRequest, headers=autenticazione)
            print(response.status_code)
            print(response.json())
        except Exception as e:
            print("Problemi di comunicazione:", str(e))

    CreaInterfaccia()
    sOper = input("Seleziona operazione: ")
