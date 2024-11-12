from flask import Flask, render_template, request

api = Flask(__name__)




utenti = [['mario','password1','M','0'], 
          ['gianni','password2','M','0'], 
          ['AnitaGaribaldi', 'pass3','F','0'] 
          ]









@api.route('/loggati', methods=['GET'])
def get_code():
    #prendi i dati della form
    nome = "mario"
    sResponsePage = "<html><body><h1>Buongiorno" + nome + " a tutti, il 17 settembre 2024</h1></body></html>"
    return sResponsePage





@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/regok', methods=['GET'])
def regOk():
    return render_template('reg_ok.html')


@api.route('/regko', methods=['GET'])
def regKo():
    return render_template('reg_ko.html')

@api.route('/registrati', methods=['GET'])
def registra():
    #prendi i dati che ti ha inviato il server

    #verifica la correttezza 


    nome = request.args.get("nome")
    #print("Nome inserito:" + nome)
    password = request.args.get("cognome")

    if request.args.get("sesso")=="1":
        sesso="M"
    else:
        sesso = "F"

    utente = []
    utente.append(nome)
    utente.append(password)
    utente.append(sesso)
    utente.append("0")

    if utente in utenti:
        index = utenti.index(utente)
        utenti[index][3]="1"
        return render_template('reg_ok.html')

    #Devo prendere tutti i dati e verificare se la terna c'è nel vettore degli utenti
    return render_template('reg_ko.html')

api.run(host="0.0.0.0",port=8085)


