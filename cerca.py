import os  
def  CercastringaInNomefile(sFile,sStringa):
    sStringaC= sStringa.lower() 
    sFileC=sFile.lower()

    if (sFileC.find(sStringaC)>=0):
        return True
    else:
        return False
sRoot=input("Inserisci  directory in cui cercare:")
sParola=input("inserisci parola da cercare:")
sOutdir=input("inserisci directory di output:")

iNumFileTrovati=0
for root, dirs, files in os.walk(sRoot):
    print(f"sto guardando: {root}: che contine: {len(dirs)}: suddir e {len(files) }: files")
    for file in files:
        print(f"Devo vedere se: {file}: contiene: {sParola}:")
        bRet=CercastringaInNomefile(file, sParola)
        if bRet==True:
            iNumFileTrovati +=1
        else:
            bRet=CercastringaInNomefile()

print(f" ho trovato file:{iNumFileTrovati} files")