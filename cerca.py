import os  
import PyPDF2
lTextExtension=[".txt",".py",".js",".csv",]
def  CercastringaInNomefile(sFile,sStringa):
    sStringaC= sStringa.lower() 
    sFileC=sFile.lower()

    if (sFileC.find(sStringaC)>=0):
        return True
    else:
        return False
def CercaStringaInTextfile(sFile,sStringa):
    with open (sFile,"r") as file1:
        sRiga=""
        sRiga=file1.readline()
        while (len(sRiga)>0):
            iRet=sRiga.lower().find(sStringa.lower())
            if(iRet>=0):
             sRiga=file1.readline()
    return False
def CercaStringaInPDFfile(sFile,sSstringa):
    return False

    
def CercaStringaInContenutoFile(sPathFile,sStringa):
    sOutFileName,sOutFileExt=os.path.splitext(sPathFile)
    if sOutFileExt.lower()in lTextExtension:
        bRet=CercaStringaInTextfile(sPathFile,sStringa)

    if sOutFileExt.lower()==".pdf":
        bRet=CercaStringaInPDFfile(sPathFile,sStringa)
    return bRet


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