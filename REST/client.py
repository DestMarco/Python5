import json, requests, sys


base_url="http://127.0.0.1:8080"

def RichiedidatiCittadino():
    nome=input("inserisci nome cittadino")
    cognome=input("inserisci cognome cittadino")
    dataNascita=input("inserisci data cittadino")
    codiceFiscale=input("inserisci codice fiscale cittadino")
    jReqiuest={"nome":nome, "cognome":cognome, "datanascita":dataNascita, "codicefiscale":codiceFiscale}
    return jReqiuest

def CreaInterfaccia ():
    print("Operazioni disponibbili")
    print ("1. Inserisci cittadino (es. atto di nascita)")
    print("2. Richiedi dati di acceso (es.cert. residenza)")
    print("3. modifica dati cittadino")
    print("4. ellimina cittadino")
    print("5. Exit")


CreaInterfaccia()
s0per=input("seleziona operazione")
while(s0per != "5"):
    if s0per=="1":
        print("Richiesta")
        api_url=base_url+"/add_cittadino"
        jsonDataRequest=RichiedidatiCittadino()
        try:
            print("ok1")
            respomse=requests.post(api_url,json=jsonDataRequest)
            print(respomse.status_code)
            print(respomse.headers["Content-Type"])
            data1=respomse.json()
            print(data1)
        except:
            print("problemi di comunicazione")
    CreaInterfaccia()
    s0per=input("seleziona operazione da 1 a 3")

