from flask import Flask, json, request

# Funzioni per la gestione del JSON
from myjson import SerializaJson, DeserializeJson

sFileAnagrafe = "./anagrafe.json"
sFileUtenti = "./utenti.json"  # File che contiene nome utente e password
api = Flask(__name__)

# Funzione per l'autenticazione
@api.route('/login', methods=['POST'])
def login():
    jRequest = request.json
    nome_utente = jRequest.get("nome_utente")
    password = jRequest.get("password")
    
    # Carica il file con gli utenti registrati
    utenti = DeserializeJson(sFileUtenti)
    
    if nome_utente in utenti and utenti[nome_utente] == password:
        return json.dumps({"Error": "000", "Msg": "Autenticazione riuscita!"}), 200
    else:
        return json.dumps({"Error": "001", "Msg": "Nome utente o password errati!"}), 401

# Funzione per aggiungere un cittadino
@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == "application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codicefiscale"]
        dAnagrafe = DeserializeJson(sFileAnagrafe)
        
        if sCodiceFiscale not in dAnagrafe:
            dAnagrafe[sCodiceFiscale] = jRequest
            SerializaJson(dAnagrafe, sFileAnagrafe)
            jResponse = {"Error": "000", "Msg": "Cittadino aggiunto con successo"}
            return json.dumps(jResponse), 200
        else:
            jResponse = {"Error": "002", "Msg": "Codice fiscale già presente in anagrafe"}
            return json.dumps(jResponse), 200
    else:
        return "Errore, formato non riconosciuto", 401

# Funzione per eliminare un cittadino
@api.route('/delete_cittadino', methods=['DELETE'])
def GestisciDeleteCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == "application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codicefiscale"]
        dAnagrafe = DeserializeJson(sFileAnagrafe)

        if sCodiceFiscale in dAnagrafe:
            del dAnagrafe[sCodiceFiscale]
            SerializaJson(dAnagrafe, sFileAnagrafe)
            jResponse = {"Error": "000", "Msg": "Cittadino eliminato con successo"}
            return json.dumps(jResponse), 200
        else:
            jResponse = {"Error": "003", "Msg": "Cittadino non trovato"}
            return json.dumps(jResponse), 404
    else:
        return "Errore, formato non riconosciuto", 401

api.run(host="127.0.0.1", port=8080)
