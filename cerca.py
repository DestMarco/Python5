import os 
sRoot=input("Inserisci directory in cui cercare")
sParola=input("inserisci parola da cercare ")
sOutdir=input("inserisci directory di output")
for root, dirs, filse in os.walk(sRoot):
    print (f"Sto guardando {root} che contiene {len(dirs)} suddir e {len(filse)} files")