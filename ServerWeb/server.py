from flask import Flask, render_template, redirect, url_for
from flask import request, render_template


api=Flask(__name__)

utenti = [["mario","rossi","mario.1424@gmail.com","1234","0"],["alessia","garibaldi","alessia.124@yohoo.it","Password01","0"],["gianni","Gianfranco","gianno.898@gmail.com","2304","0"]]




@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@api.route('/pippo', methods=['GET'])
def index2():
    return render_template('index2.html')

@api.route('/accedi', methods=['GET'])
def accesso():

    nome = request.args.get("nome")
    password = request.args.get("password")
    cognome=request.args.get("cognome")

    if nome and password and cognome:  
        
        for utente in utenti:
            if utente[0] == nome and  utente[3]==password and utente[1]==cognome and utente[-1] == "1"  :
                
                return redirect(url_for('accesso_successo', nome=nome, password=password, cognome=cognome))

        return redirect(url_for('accesso_fallito'))
    return render_template('accedi.html')


 

@api.route('/accesso_successo', methods=['GET'])
def accesso_successo():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    return render_template('accessoS.html', nome=nome, cognome=cognome)

@api.route('/accesso_fallito', methods=['GET'])
def accesso_fallito():
    return render_template('accessoF.html')






@api.route('/reggistrati', methods=['GET'])
def registra():
    nome=request.args.get("nome")

    cognome=request.args.get("cognome")

    email=request.args.get("email")


    password=request.args.get("password")
    l: list[str] =[nome,cognome,email,password,"0"]

    for i in utenti:
        if l==i:
            i[-1]="1"
            return render_template('reg_ok.html')
        
    return render_template('reg_ko.html')
 
       




        

    

@api.route('/reok', methods=['GET'])
def reg_ok():
    return render_template('reg_ok.html')







api.run(host="0.0.0.0",port=8085)