def lectura (lista,nodo):
    a=[]
    b=[]
    for i in lista:
        if(nodo==i[0]):
            if(i[1]=="a"):
                a.append(i[2])
            if(i[1]=="b"):
                b.append(i[2])
            if(i[1]==""):
                aux=lectura(lista,i[2])
                a.append(aux[0])
                b.append(aux[1])
                
    return (a,b)
    




E=["a","b"]
L=[("Q0","a","Q2"),
   ("Q0","b","Q0"),
   ("Q0","","Q1"),
   ("Q1","a","Q4"),
   ("Q1","b","Q1"),
   ("Q2","a","Q0"),
   ("Q3","a","Q1"),
   ("Q4","a","Q4")]

K=["Q0","Q1","Q2","Q3","Q4"]
S=["Q0","Q1"]
F=["Q4"]

M=[K,E,S,L,F]

AFD=[]
ColA=[]
ColB=[]
for var in K:
    aux=lectura(L,var)
    ColA.append(aux[0])
    ColB.append(aux[1])

print (ColA,"\n",ColB)
