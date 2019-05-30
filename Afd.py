#!/usr/bin/env python
# -*- coding: utf-8 -*-

from AutomataFinito import AutomataFinito
tabla={}
class Afd(AutomataFinito):
    def __init__(self, afnd):
        AutomataFinito.__init__(self, afnd.K, afnd.S, afnd.s, afnd.F, afnd.d)
        self.afndAAfd(afnd.tablaDeTransicion(), afnd.s, afnd.F)
        #AutomataFinito.__init__(self, K, S, s, F, d)

    # Se crea un elemento de la tabla comenzando por la etiqueta
    def procesarNodo(self, nodo, AFND, tabla, finales):
        etiquetaNodo = self.multinodoAEtiqueta(nodo)
        tabla[etiquetaNodo] = {}

        estaFinal = False
        for final in finales:
            if (final in nodo):
                estaFinal = True
        if (estaFinal):
            self.F = self.combinarListas(self.F, [nodo])

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
                    self.procesarNodo(tabla[etiquetaNodo][caracter], AFND, tabla, finales)
        return tabla
    
        # Se define el nodo inicial
    def afndAAfd(self, tablaTransicion, nodosInicialesAfnd, nodosFinalesAfnd):
        nodoInicial = []

        self.F = []

        for nodo in nodosInicialesAfnd:
            nodoInicial.append(nodo)
            nodoInicial = self.combinarListas(nodoInicial, self.conexionesConVacio(nodo))

        self.s = [nodoInicial]


        #Teniendo el nodo inicial se llama la función recursiva para completar la tabla
        self.procesarNodo(nodoInicial, tablaTransicion, tabla, nodosFinalesAfnd)

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
        
        self.d = self.diccionarioATuplas(tabla)

    def diccionarioATuplas(self, diccionario):
        lista = []
        for k1 in diccionario.keys():
            for k2 in diccionario[k1].keys():
                tupla = (k1, k2, diccionario[k1][k2])
                lista.append(tupla)
        return lista
                
    
    def caracterEstaEnAlfabeto(self, caracter):
        #Recorre la lista
        for c in self.S:
            if (caracter == c):
                return True
        else:
            return False

    #Funcion que entrega un true si la palabra se puede comparar con el lenguaje y false si no
    def palabraEsComparable(self, palabra):
        for letra in palabra:
            if (self.caracterEstaEnAlfabeto(letra) != True):
                return False
        return True

        
    def leer(self, palabra):
        ########################################################################################
        #POR MEJORAR (se esta obteniendo el inicio del diccionario, la clave, con trampita u.u)
        clave = self.multinodoAEtiqueta(self.s)
        auxnum = 0
        if (self.palabraEsComparable(palabra)):
            for letra in palabra:
                aux = "".join(str(x) for x in tabla[clave][letra])
                if (aux != "S"):
                    clave = aux
                else:
                    auxnum = 1
                    print("La palabra NO pertenece al lenguaje")
                    break
            if (auxnum == 0):
                print("La palabra pertenece al lenguaje")
        else:
            print ("La palabra NO pertenece al lenguaje")
    