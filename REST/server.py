from flask import Flask, json, request
from myjson import SerializaJson, DeserializeJson

sFileAnagrafe = "./anagrafe.json"
api = Flask(__name__)

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-type')
    print("ricevuta chiamata " + content_type)
    if content_type == "application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codicefiscale"]
        print("ricevuto " + sCodiceFiscale)
        dAnagrafe = DeserializeJson(sFileAnagrafe)
        if sCodiceFiscale not in dAnagrafe:
            dAnagrafe[sCodiceFiscale] = jRequest
            SerializaJson(dAnagrafe, sFileAnagrafe)
            jResponse = {"Error": "000", "Msg": "ok"}
            return json.dumps(jResponse), 200
        else:
            jResponse = {"Error": "001", "Msg": "Codice fiscale già presente in anagrafe"}
            return json.dumps(jResponse), 200
    else:
        return "Errore, formato non riconosciuto", 401

@api.route('/update_cittadino', methods=['PUT'])
def GestisciModificaCittadino():
    content_type = request.headers.get('Content-type')
    if content_type == "application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codicefiscale"]
        dAnagrafe = DeserializeJson(sFileAnagrafe)
        if sCodiceFiscale in dAnagrafe:
            dAnagrafe[sCodiceFiscale] = jRequest
            SerializaJson(dAnagrafe, sFileAnagrafe)
            jResponse = {"Error": "000", "Msg": "Cittadino modificato con successo"}
            return json.dumps(jResponse), 200
        else:
            jResponse = {"Error": "002", "Msg": "Cittadino non trovato"}
            return json.dumps(jResponse), 404
    else:
        return "Errore, formato non riconosciuto", 401

@api.route('/delete_cittadino', methods=['DELETE'])
def GestisciEliminaCittadino():
    content_type = request.headers.get('Content-type')
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
            jResponse = {"Error": "002", "Msg": "Cittadino non trovato"}
            return json.dumps(jResponse), 404
    else:
        return "Errore, formato non riconosciuto", 401

api.run(host="127.0.0.1", port=8080)
