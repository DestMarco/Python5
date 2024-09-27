from flask import Flask, json, request

from myjson import SerializaJson, DeserializeJson

sFileAnagrafe="./anagrafe.json"
api=Flask(__name__)

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type=request.headers.get('Content-type')
    print("ricevuta chiamata" + content_type)
    if content_type=="application/json":
        jRequest=request.json
        sCodiceFiscale=jRequest["codicefiscale"]
        print("ricevuto" + sCodiceFiscale)
        dAnagrafe=DeserializeJson(sFileAnagrafe)
        if sCodiceFiscale not in dAnagrafe:
            dAnagrafe[sCodiceFiscale] = jRequest
            SerializaJson(dAnagrafe,sFileAnagrafe)
            jResponse={"Error":"000","Msg":"ok"}
            return json.dumps(jResponse),200
        else:
            jResponse={"Error":"000","Msg":"codice fiscale gia presente in anagrafe"}
            return json.dumps(jResponse),200
        
    else:
        return "Errore, formato non riconosciuto",401

api.run(host="127.0.0.1", port=8080)
