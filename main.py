def combinarListas(l1, l2):
    aux = l1
    if type(l2) == list:
        aux.extend(l2)
    else:
        aux.append(l2)
    listaFinal = []
    for elemento in aux:
        try:
            listaFinal.index(elemento)
        except ValueError:
            listaFinal.append(elemento)
    return listaFinal

def conexionesConVacio(lista, nodo):
    nodosVacios = []
    for tupla in lista:
        if(nodo == tupla[0] and tupla[1] == ""):
            nodosVacios = combinarListas(nodosVacios, tupla[2])
            nodosVacios = combinarListas(nodosVacios, conexionesConVacio(lista, tupla[2]))
    return nodosVacios

def procesarNodo(lista, alfabeto, nodo):
    diccionario = {}

    for tupla in lista:
        if (nodo == tupla[0]):
            for caracter in alfabeto:
                if (tupla[1] == caracter):
                    if caracter not in diccionario:
                        diccionario[caracter] = []
                    
                    diccionario[caracter]= combinarListas(diccionario[caracter],tupla[2])
                    diccionario[caracter]= combinarListas(diccionario[caracter], conexionesConVacio(lista, tupla[2]))

            if(tupla[1] == ""):
                aux=procesarNodo(lista, alfabeto, tupla[2])
                for c, e in aux.items():
                    if c in diccionario:
                        diccionario[c] = combinarListas(diccionario[c], e)
                    else:
                        diccionario[c] = []
                        diccionario[c] = combinarListas(diccionario[c], e)
    return diccionario


E=["a","b"]
L=[("Q0","a","Q2"),
   ("Q0","b","Q0"),
   ("Q0","","Q1"),
   ("Q1","a","Q4"),
   ("Q1","b","Q1"),
   ("Q2","a","Q0"),
   ("Q3","a","Q1"),
   ("Q4","a","Q4"),
   ("Q1", "", "Q8")]

K=["Q0","Q1","Q2","Q3","Q4", "Q8"]
S=["Q0"]
F=["Q4"]

M=[K,E,S,L,F]

AFD=[]

tabla = {}

for nodo in K:
    aux=procesarNodo(L, E, nodo)
    tabla[nodo] = aux
    print(aux)
