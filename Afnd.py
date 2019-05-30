#!/usr/bin/env python3
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
                        
                        diccionario[caracter] = self.combinarListas(diccionario[caracter], tupla[2])
                        diccionario[caracter] = self.combinarListas(diccionario[caracter], self.conexionesConVacio(tupla[2]))

                if (tupla[1] == ""):
                    aux = self.procesarNodo(lista, alfabeto, tupla[2])
                    for c, e in aux.items():
                        if c in diccionario:
                            diccionario[c] = self.combinarListas(diccionario[c], e)
                        else:
                            diccionario[c] = []
                            diccionario[c] = self.combinarListas(diccionario[c], e)
        return diccionario

    def tablaDeTransicion(self):
        tabla = {}
        for nodo in self.K:
            aux = self.procesarNodo(self.d, self.S, nodo)
            tabla[nodo] = aux
        return tabla
