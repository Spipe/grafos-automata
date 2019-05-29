#!/usr/bin/env python
# -*- coding: utf-8 -*-

from AutomataFinito import AutomataFinito

class Afnd(AutomataFinito):
    def __init__(self, K, S, s, F, d):
        AutomataFinito.__init__(self, K, S, s, F, d)
        
    # Se crea un diccionario para guardar las listas de nodos que se podrán leer con cada carácter
    def procesarNodo(self, lista, alfabeto, nodo):
        diccionario = {}

        # Se recorre la lista y compara que el primer elemento de la tupla sea el nodo ingresado
        # Si el carácter no existe en el diccionario, se crea
        for tupla in lista:
            if (nodo == tupla[0]):
                for caracter in alfabeto:
                    if (tupla[1] == caracter):
                        if caracter not in diccionario:
                            diccionario[caracter] = []
                        
                        diccionario[caracter] = combinarListas(diccionario[caracter],tupla[2])
                        diccionario[caracter] = combinarListas(diccionario[caracter], self.conexionesConVacio(lista, tupla[2]))

                if (tupla[1] == ""):
                    aux = self.procesarNodo(lista, alfabeto, tupla[2])
                    for c, e in aux.items():
                        if c in diccionario:
                            diccionario[c] = combinarListas(diccionario[c], e)
                        else:
                            diccionario[c] = []
                            diccionario[c] = combinarListas(diccionario[c], e)
        return diccionario


    # Se define el nodo inicial
    def transformarAAfd(AFND, lista, nodo, alfabeto):
        tabla = {}
        nodoInicial = [nodo]
        nodoInicial = combinarListas(nodoInicial, conexionesConVacio(lista, nodo))

        #Teniendo el nodo inicial se llama la función recursiva para completar la tabla
        etiqueta = etiquetas(nodoInicial)
        procesarNodoAFD(nodoInicial, AFND, tabla)

        haySumidero = False

        #Se comprueba la existencia de cada carácter por nodo en el diccionario
        for caracter in alfabeto:
            for nodoAux in tabla:
                if caracter not in tabla[nodoAux]:
                    tabla[nodoAux][caracter] = ["S"]
                    haySumidero = True
        
        #En caso de existir el sumidero, este se agrega
        if haySumidero:
            diccionarioAux = {}
            for caracter in alfabeto:
                diccionarioAux[caracter] = ["S"]
            tabla["S"] = diccionarioAux
        
        return tabla

    def tablaDeTransicion(self):
        print("Holadasdsa")
        tabla = {}
        for nodo in self.K:
            aux = self.procesarNodo(self.d, self.S, nodo)
            tabla[nodo] = aux
            print(aux)
        return tabla