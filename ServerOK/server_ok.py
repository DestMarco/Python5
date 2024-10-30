from flask import Flask, jsonify, request
from myjson import JsonDeserialize, JsonSerialize
import sys
import dbclient as db

from flask import Flask, jsonify, request
import dbclient as db
import sys

app = Flask(__name__)

# Connessione al database
cur = db.connect()
if cur is None:
    print("Errore di connessione al DB")
    sys.exit()

# Login utente
@app.route('/login', methods=['POST'])
def GestisciLogin():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        username = jsonReq.get("username")
        password = jsonReq.get("password")
        
        query = f"SELECT privilegi FROM utenti WHERE username='{username}' AND password='{password}';"
        cur.execute(query)
        result = cur.fetchone()
        
        if result:
            return jsonify({"Esito": "000", "Msg": "Utente registrato", "Privilegio": result[0]}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Credenziali errate"}), 401
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta errato"}), 400

# Inserimento cittadino
@app.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json.get('datiCittadino')
        codice_fiscale = jsonReq.get("codFiscale")
        nome = jsonReq.get("nome")
        cognome = jsonReq.get("cognome")
        data_nascita = jsonReq.get("dataNascita")
        
        query = f"INSERT INTO anagrafe (codice_fiscale, nome, cognome, data_nascita) VALUES ('{codice_fiscale}', '{nome}', '{cognome}', '{data_nascita}');"
        
        result = db.write_in_db(cur, query)
        if result == 0:
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiunto con successo"}), 200
        else:
            return jsonify({"Esito": "002", "Msg": "Errore durante l'inserimento"}), 500
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta errato"}), 400

# Lettura cittadino
@app.route('/read_cittadino/<codice_fiscale>', methods=['GET'])
def read_cittadino(codice_fiscale):
    query = f"SELECT * FROM anagrafe WHERE codice_fiscale='{codice_fiscale}';"
    cur.execute(query)
    result = cur.fetchone()
    
    if result:
        cittadino = {
            "codFiscale": result[0],
            "nome": result[1],
            "cognome": result[2],
            "dataNascita": result[3].strftime('%Y-%m-%d')
        }
        return jsonify({"Esito": "000", "Msg": "Cittadino trovato", "Dati": cittadino}), 200
    else:
        return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 404

# Modifica cittadino
@app.route('/update_cittadino', methods=['PUT'])
def update_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get("codFiscale")
        nome = jsonReq.get("nome")
        cognome = jsonReq.get("cognome")
        data_nascita = jsonReq.get("dataNascita")
        
        query = f"UPDATE anagrafe SET nome='{nome}', cognome='{cognome}', data_nascita='{data_nascita}' WHERE codice_fiscale='{codice_fiscale}';"
        
        result = db.write_in_db(cur, query)
        if result == 0:
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiornato con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Errore durante l'aggiornamento"}), 500
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta errato"}), 400

# Eliminazione cittadino
@app.route('/elimina_cittadino', methods=['DELETE'])
def elimina_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        codice_fiscale = request.json.get("codFiscale")
        
        query = f"DELETE FROM anagrafe WHERE codice_fiscale='{codice_fiscale}';"
        result = db.write_in_db(cur, query)
        
        if result == 0:
            return jsonify({"Esito": "000", "Msg": "Cittadino eliminato con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Errore durante l'eliminazione"}), 500
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta errato"}), 400

# Avvio server
app.run(host="0.0.0.0", port=8080, ssl_context="adhoc")
