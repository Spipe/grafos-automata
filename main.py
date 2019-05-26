#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
            # En caso de multiples conexiones vacías:
            # nodosVacios = combinarListas(nodosVacios, conexionesConVacio(lista, tupla[2]))
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

def opciones():
    print("\n\tMenu principal")
    print("(1) ")
    print("(2)")
    print("(3)")
    print("(4)")
    print("(0) Salir")

def menu():
    while True:
        opciones()
        opcion = input("Ingrese una opcion: ")

        if opcion == 1:
            print("Opcion 1")
        elif opcion == 2:
            print("Opcion 2")
        elif opcion == 3:
            print("Opcion 3")
        elif opcion == 4:
            print("Opcion 4")
        elif opcion == 0:
            break
        else:
            print("Opcion invalida")

def main():
    print("Grafos y lenguajes formales\n21041|INFB8061-1\n\nTrabajo 2: Automata\n")
    print("Integrantes:\n")
    print("- Felipe Flores Vivanco\n- Andres Mella\n- Jorge Verdugo Chacon\n- Javiera Vergara Navarro")
    menu()


##Datos de prueba:

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
S=["Q0"]
F=["Q4"]

M=[K,E,S,L,F]

AFD=[]

tabla = {}

for nodo in K:
    aux=procesarNodo(L, E, nodo)
    tabla[nodo] = aux
    print(aux)

#Llamada del main, se comenta por mientras uwu
#main()