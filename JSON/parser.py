
import ast

mylist_1="['mario', 'gino', 'lucrezia']"

mylist_2=['mario', 'gino' , 'lucrezia']

var=mylist_1[1]

var1=mylist_2[1]
type(var1)


def SerializzaLista(lVar) -> str:

    lVar=str(lVar)
    return lVar


def DeserializzaLista(sVar) -> str:
    try:
        
        return ast.literal_eval(sVar)
    except (ValueError, SyntaxError):
        print("Invalid string format")
        return []
        
serializza=SerializzaLista(mylist_2)
print("Serialized", serializza)


deserializza=DeserializzaLista(mylist_1)
print("Deserialized:", deserializza)




