import requests, json, sys

import requests
import sys

base_url = "https://127.0.0.1:8080"

# Variabili per salvare le credenziali dell'utente
sUsername = ""
sPassword = ""

# Funzioni di utilità per gestire input e output
def GetDatiCittadino():
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    dataN = input("Inserisci la data di nascita (gg/mm/aaaa): ")
    codF = input("Inserisci il codice fiscale: ")
    return {
        "nome": nome,
        "cognome": cognome,
        "dataNascita": dataN,
        "codFiscale": codF
    }

def GetCodicefiscale():
    cod = input("Inserisci codice fiscale: ")
    return {"codFiscale": cod}

def EseguiOperazione(iOper, sServizio, dDatiToSend):
    try:
        # Esegui la richiesta POST
        response = requests.post(sServizio, json=dDatiToSend, verify=False)
        
        # Gestisci la risposta
        if response.status_code == 200:
            print(response.json())
        else:
            print("Errore durante l'operazione. Codice di errore:", response.status_code)
    except Exception as e:
        print("Errore di comunicazione con il server:", e)

# Funzione per il login iniziale dell'utente
def EffettuaPrimoLogin():
    global sUsername, sPassword
    sUsername = input("Inserisci username: ")
    sPassword = input("Inserisci password: ")

    jsonRequest = {"username": sUsername, "password": sPassword}

    try:
        response = requests.post(f"{base_url}/login", json=jsonRequest, verify=False)
        if response.status_code == 200:
            jsonResponse = response.json()
            if jsonResponse["Esito"] == "000":
                print("Login avvenuto con successo!")
                return True
            else:
                print("Errore login:", jsonResponse["Msg"])
                return False
        else:
            print("Errore durante il login. Codice di errore:", response.status_code)
            return False
    except Exception as e:
        print("Errore di comunicazione con il server:", e)
        return False

# Inizio applicazione client
print("Benvenuti al Comune - sede locale")

# Effettua il login finché non è valido
login_effettuato = False
while not login_effettuato:
    login_effettuato = EffettuaPrimoLogin()

# Loop principale per le operazioni
while True:
    print("\nOperazioni disponibili:")
    print("1. Inserisci cittadino")
    print("2. Richiedi cittadino")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    print("5. Esci")

    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue

    # Parametri comuni per ogni richiesta
    api_url = ""
    jsonDataRequest = {"username": sUsername, "password": sPassword}

    # Aggiungi cittadino
    if iOper == 1:
        print("Aggiunta cittadino")
        api_url = f"{base_url}/add_cittadino"
        jsonDataRequest["datiCittadino"] = GetDatiCittadino()
        EseguiOperazione(iOper, api_url, jsonDataRequest)

    # Richiesta dati cittadino
    elif iOper == 2:
        print("Richiesta dati cittadino")
        api_url = f"{base_url}/read_cittadino"
        jsonDataRequest.update(GetCodicefiscale())
        EseguiOperazione(iOper, api_url, jsonDataRequest)

    # Modifica cittadino
    elif iOper == 3:
        print("Modifica cittadino")
        api_url = f"{base_url}/update_cittadino"
        jsonDataRequest.update(GetDatiCittadino())
        EseguiOperazione(iOper, api_url, jsonDataRequest)

    # Eliminazione cittadino
    elif iOper == 4:
        print("Eliminazione cittadino")
        api_url = f"{base_url}/elimina_cittadino"
        jsonDataRequest.update(GetCodicefiscale())
        EseguiOperazione(iOper, api_url, jsonDataRequest)

    # Esci
    elif iOper == 5:
        print("Buona giornata!")
        break
    else:
        print("Operazione non disponibile, riprova.")
