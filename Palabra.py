from main import AFD
from main import procesarNodo

E=["a","b"]
#Ejemplo con el ejercicio de la prueba
L=[("Q0", "a", "Q2"),
    ("Q0", "b", "Q0"),
    ("Q0", "", "Q1"),
    ("Q2", "a", "Q0"),
    ("Q4", "a" "Q3"),
    ("Q1", "b", "Q1"),
    ("Q3", "a", "Q1"),
    ("Q1", "", "Q4")]
K=["Q0","Q1","Q2","Q3","Q4"]
S=["Q0"]
F=["Q1"]

tabla = {}

for nodo in K:
    aux=procesarNodo(L, E, nodo)
    tabla[nodo] = aux

afd=AFD(tabla, L, S[0], E)
#Funcion que compara un caracter en una lista
def comparar(caracter):
    #Recorre la lista
    for i in E:
        if(caracter==i):
            return True
    else:
        return False

#Funcion que entrega un true si la palabra se puede comparar con el lenguaje y false si no
def lectura(palabra):
    for letra in palabra:
        if(comparar(letra)!=True):
            return False
    return True

     
def recorrido(palabra):
    ########################################################################################
    #POR MEJORAR (se esta obteniendo el inicio del diccionario, la clave, con trampita u.u)
    clave='Q0Q1Q4' 
    auxnum=0
    if(lectura(palabra)):
        for letra in palabra:
            aux="".join(str(x) for x in afd[clave][letra])
            if(aux!="S"):
                clave=aux
            else:
                auxnum=1
                print ("La palabra NO pertenece al lenguaje")
                break
        if(auxnum==0):
            print("La palabra pertenece al lenguaje")
        
    else:
        print ("La palabra NO pertenece al lenguaje")


recorrido("aabaaba")
