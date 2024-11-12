import sys
import os
import os.path
import time

#pip3 install psycopg2-binary
import dbclient as db


print("Inizio programma prova database")
cur = db.connect()
if cur is None:
	print("Errore connessione al DB")
	sys.exit()


#sQuery = "insert into cittadini ............"
#db.write_in_db(cur,sQuery)


sQuery = "select * from ordini limit 5;"
iNumRows = db.read_in_db(cur,sQuery)
print("Numero di righe: " + str(iNumRows))
for ii in range(0,iNumRows):
	myrow = db.read_next_row(cur)
	print(myrow)
	