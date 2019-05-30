#!/usr/bin/env python
# -*- coding: utf-8 -*-

from AutomataFinito import AutomataFinito

class Afd(AutomataFinito):
    def __init__(self, afnd):
        AutomataFinito.__init__(self, afnd.K, afnd.S, afnd.s, afnd.F, afnd.d)
        self.afndAAfd(afnd.tablaDeTransicion(), afnd.s[0])
        #AutomataFinito.__init__(self, K, S, s, F, d)

    # Se crea un elemento de la tabla comenzando por la etiqueta
    def procesarNodo(self, nodo, AFND, tabla):
        etiquetaNodo = self.multinodoAEtiqueta(nodo)
        tabla[etiquetaNodo] = {}

        #Por cada elemento que componga el nodo, se recorre AFND para crear los conjuntos
        #de nodos a los que se puedan conectar mediante el alfabeto
        #Luego llama recursivamente la función cambiando el nodo del parámetro

        for elemento in nodo:
            for caracter in AFND[elemento].keys():
                if caracter not in tabla[etiquetaNodo]:
                    tabla[etiquetaNodo][caracter] = []
                tabla[etiquetaNodo][caracter] = self.combinarListas(tabla[etiquetaNodo][caracter], AFND[elemento][caracter])
                etiqueta = self.multinodoAEtiqueta(tabla[etiquetaNodo][caracter])
                if etiqueta not in tabla:
                    self.procesarNodo(tabla[etiquetaNodo][caracter], AFND, tabla)
        return tabla
    
        # Se define el nodo inicial
    def afndAAfd(self, tablaTransicion, nodoInicialAfnd):
        tabla = {}
        nodoInicial = [nodoInicialAfnd]
        nodoInicial = self.combinarListas(nodoInicial, self.conexionesConVacio(nodoInicialAfnd))

        #Teniendo el nodo inicial se llama la función recursiva para completar la tabla
        self.procesarNodo(nodoInicial, tablaTransicion, tabla)

        haySumidero = False

        #Se comprueba la existencia de cada carácter por nodo en el diccionario
        for caracter in self.S:
            for nodoAux in tabla:
                if caracter not in tabla[nodoAux]:
                    tabla[nodoAux][caracter] = ["S"]
                    haySumidero = True
        
        #En caso de existir el sumidero, este se agrega
        if haySumidero:
            diccionarioAux = {}
            for caracter in self.S:
                diccionarioAux[caracter] = ["S"]
            tabla["S"] = diccionarioAux
        
        print(tabla)
        return tabla