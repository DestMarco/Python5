from flask import Flask, render_template
from flask import request, render_template


api=Flask(__name__)

utenti = [["mario","rossi","mario.1424@gmail.com","1234"],["alessia","garibaldi","alessia.124@yohoo.it","Password01"],["gianni","Gianfranco","gianno.898@gmail.com","2304"]]

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@api.route('/pippo', methods=['GET'])
def index2():
    return render_template('index2.html')



@api.route('/reggistrati', methods=['GET'])
def registra():
    nome=request.args.get("nome")
    print("Nome Inserito:"+ nome)

    cognome=request.args.get("cognome")
    print("Cognome inserito:"+cognome)

    email=request.args.get("email")
    print("email inserito:"+email)

    password=request.args.get("password")
    print("Password inserita:"+password)
    l: list[str] =[nome,cognome,email,password]

    for i in utenti:
        if l==i:
            return render_template('reg_ok.html')
    
    return render_template('reg_ko.html')


        

    


@api.route('/reok', methods=['GET'])
def reg_ok():
    return render_template('reg_ok.html')







api.run(host="0.0.0.0",port=8085)