from flask import Flask, jsonify, request
from myjson import JsonDeserialize, JsonSerialize
import sys
import dbclient as db

api = Flask(__name__)

#Devo connettermi al database
cur = db.connect()
if cur is None:
	print("Errore connessione al DB")
	sys.exit()


file_path = "anagrafe.json"
cittadini = JsonDeserialize(file_path)

file_path_users = "utenti.json"
utenti = JsonDeserialize(file_path_users)


def MiaProcedura():
    print("Buongiorno a tutti")






@api.route('/login', methods=['POST'])
def GestisciLogin():
    global cur
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        sUsernameInseritoDalClient = jsonReq["username"]
        sPasswordInseritaDalClient = jsonReq["password"]
        sQuery = "select privilegi from utenti where mail='" + sUsernameInseritoDalClient + "' and password='" + sPasswordInseritaDalClient + "';"  
        print(sQuery)
        iNumRows = db.read_in_db(cur,sQuery)
        if iNumRows == 1:
            #[0,['w']] questo è lRow
            # 0 è lRow[0] 
            #['w'] questo è lRow[1]
            #'w' è lRow[1][0]

            #Se la query fosse stata      select mail,privilegi
            #[0,['mariorossi@gmail.com','w']]

            lRow = db.read_next_row(cur)
            sPriv = lRow[1][0]
            print("privilegio: " + sPriv)
            return jsonify({"Esito": "000", "Msg": "Utente registrato", "Privilegio":sPriv}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Credenziali errate"})
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta errato"}) 





@api.route('/add_cittadino', methods=['POST', 'GET'])
def GestisciAddCittadino():
    global cur
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        
        #prima di tutto verifico utente, password e privilegio 
        #dove utente e password me l'ha inviato il client
        #mentre il privilegio lo vado a leggere nel mio file  (utenti.json)

        codice_fiscale = jsonReq.get('codFiscale')
        nome = jsonReq.get('nome')
        cognome = jsonReq.get('cognome')
        dataNascita = jsonReq.get('dataNascita')
        
        sQuery = "insert into anagrafe(codice_fiscale,nome,cognome,data_nascita) values ("
        sQuery += "'" + codice_fiscale + "','" + nome + "','" + cognome + "','" + dataNascita + "');"
        
        
        print(sQuery)
        
        
        
        iRet = db.write_in_db(cur,sQuery)
        if iRet == -2:
            return jsonify({"Esito": "001", "Msg": "Cittadino già esistente"}), 200
        elif iRet == -1:
            return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200
        else:
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiunto con successo"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200



"""
Questa funzione sta sul SERVER. Riceve il codice fiscale dal client 
e verifica se il codice e d i dati associati stanno in anagrafe.json
"""

@api.route('/read_cittadino/<codice_fiscale>/<username>/<password>', methods=['GET'])
def read_cittadino(codice_fiscale,username,password):

    #prima di tutto verifico utente, password e privilegio 
    #dove utente e password me l'ha inviato il client
    #mentre il privilegio lo vado a leggere nel mio file  (utenti.json)
    sQuery = "select * from cittadini where codice_fiscale='" + codice_fiscale + "';"
    
    cittadino = cittadini.get(codice_fiscale)
    if cittadino:
        return jsonify({"Esito": "000", "Msg": "Cittadino trovato", "Dati": cittadino}), 200
    else:
        return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200






@api.route('/update_cittadino', methods=['PUT'])
def update_cittadino():

    #prima di tutto verifico utente, password e privilegio 
    #dove utente e password me l'ha inviato il client
    #mentre il privilegio lo vado a leggere nel mio file  (utenti.json)

    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            cittadini[codice_fiscale] = jsonReq
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiornato con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200


@api.route('/elimina_cittadino', methods=['DELETE'])
def elimina_cittadino():

    #prima di tutto verifico utente, password e privilegio 
    #dove utente e password me l'ha inviato il client
    #mentre il privilegio lo vado a leggere nel mio file  (utenti.json)
    
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        cod = request.json.get('codFiscale')
        if cod in cittadini:
            del cittadini[cod]
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino rimosso con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200


api.run(host="0.0.0.0", port=8080, ssl_context="adhoc")

