
import ast, json

mylist_1="['mario', 'gino', 'lucrezia']"

mylist_2=['mario', 'gino' , 'lucrezia']

var=mylist_1[1]

var1=mylist_2[1]
type(var1)


def SerializzaLista(lVar) -> str:

    lVar=str(lVar)
    return lVar


def DeserializzaLista(sVar) :
    try:
        
        return ast.literal_eval(sVar)
    except (ValueError, SyntaxError):
        print("Invalid string format")
        return []
        



serializza=SerializzaLista(mylist_2)
print(type(serializza))
print ("serializza:", serializza)


deserializza=DeserializzaLista(mylist_1)
print(type(deserializza))
print("deserializza:", deserializza)


mydict_1 = { "brand": "Ford",

"electric": False,

"year": 1964,

"colors": ["red", "white", "blue"]}



mydict_2 = "{ 'brand':   'Ford'," + \
"'electric': False," + \
"'year': 1964," + \
"'colors': ['red', 'white', 'blue']}"  



def SerializaJson(dData, file_path) -> bool:

    try:
        # Scrive il dizionario in un file JSON
        with open(file_path, 'w') as file:
            json.dump(dData, file, indent=4)
        return True
    except Exception as e:
        print(f"Errore durante la serializzazione: {e}")
        return False

def DeserializeJson(file_path) -> dict:

    try:
        # Legge e converte il contenuto JSON in un dizionario
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Errore durante la deserializzazione: {e}")
        return {}


# Serializzazione del dizionario in un file JSON
file_path = "./mydict.json"
if SerializaJson(mydict_1, file_path):
    print("Dizionario serializzato con successo.")
else:
    print("Errore nella serializzazione.")

# Deserializzazione dal file JSON
mydict_deserialized = DeserializeJson(file_path)
if mydict_deserialized:
    print("Dizionario deserializzato con successo:", mydict_deserialized)
else:
    print("Errore nella deserializzazione.")
