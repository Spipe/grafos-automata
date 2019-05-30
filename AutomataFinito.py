#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AutomataFinito:
    def __init__(self, K, S, s, F, d):
        self.K = K
        self.S = S
        self.s = s 
        self.F = F
        self.d = d

    # Se toman dos listas y se comprueba que la segunda sea del tipo "lista" antes de agregarlo
    def combinarListas(self, l1, l2):
        aux = l1
        if type(l2) == list:
            aux.extend(l2)
        else:
            aux.append(l2)
        
        #Se comprueba si es que los elementos de la unión no se repiten
        #Si el elemento de la unión no existe en la lista final, se agrega
        listaFinal = []
        for elemento in aux:
            try:
                listaFinal.index(elemento)
            except ValueError:
                listaFinal.append(elemento)
        return listaFinal
    
    # Devuelve una lista con los nodos que se ven unidos por un vacío al nodo de entrada
    def conexionesConVacio(self, nodo):
        nodosVacios = []
        for tupla in self.d:
            if(nodo == tupla[0] and tupla[1] == ""):
                nodosVacios = self.combinarListas(nodosVacios, tupla[2]) 
                nodosVacios = self.combinarListas(nodosVacios, self.conexionesConVacio(tupla[2]))
        return nodosVacios
    
    # Devuelve el nombre en string que recibe un nodo
    def multinodoAEtiqueta(self, multinodo):
        etiqueta = ''
        for nodo in multinodo:
            etiqueta += nodo
        return etiqueta
    
