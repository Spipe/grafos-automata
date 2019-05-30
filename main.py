#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from Afnd import Afnd
from Afd import Afd

#Listas de la quintupla
E=[]
L=[]
K=[]
S=[]
F=[]

# Aquí comienza el main##
def opciones():
    print("\n\tMenu principal.")
    print("(1) Crear un AFND. ")
    print("(2) Obtener la quintupla del AFND ingresado")
    print("(3) Comprobar que una palabra puede ser leida por el automata.")
    print("(4) Obtener la quintupla del AFD equivalente")
    print("(5) Obtener el AFND minimo")
    print("(0) Salir.")

#Limpia la pantalla
def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def mostrarNodos(K):
    for i in range(len(K)):
        print("(" +  str(i + 1) + ") Q" + str(i))

def mostrarAlfabeto(E):
    for i in range(len(E)):
        print("(" + str(i + 1) + ") " + str(E[i]))

def crearAutomata():
    nodos = 0
    print("NODOS\n")
    print("¿Cuántos nodos tiene tu AFND?")
    nodos = input("Ingrese un número: ")
    nodos = int(nodos)
    lista = []
    for i in range(nodos):
        lista.append("Q" + str(i))
    K = lista
    borrarPantalla()

    alfabeto = []
    print("ALFABETO\n")

    caracter = input("Ingrese un caracter del alfabeto (vacío para terminar): ")
    caracter = str(caracter)

    while (caracter != ""):
        alfabeto.append(caracter)
        caracter = input("Ingrese un caracter del alfabeto (vacío para terminar): ")
        caracter = str(caracter)
    E = alfabeto
    borrarPantalla()

    nodosIniciales = []
    print("NODOS INICIALES\n")

    mostrarNodos(K)

    seguir = True
    while (seguir):
        opcion = input("Ingrese una opción (vacío para terminar): ")
        if (opcion != ""):
            opcion = int(opcion)

            while (opcion < 1 or opcion > len(K)):
                print("Error")
                opcion = input("Ingrese una opcion (vacío para terminar):")
                if (opcion == ""):
                    seguir = False
                else:
                    opcion = int(opcion)

            nodosIniciales.append(K[opcion - 1])
        else:
            seguir = False
    S = nodosIniciales
    borrarPantalla()

    nodosFinales = []
    print("NODOS FINALES\n")

    mostrarNodos(K)

    seguir = True
    while (seguir):
        opcion = input("Ingrese una opción (vacío para terminar): ")
        if (opcion != ""):
            opcion = int(opcion)

            while (opcion < 1 or opcion > len(K)):
                print("Error")
                opcion = input("Ingrese una opcion (vacío para terminar):")
                if (opcion == ""):
                    seguir = False
                else:
                    opcion = int(opcion)

            nodosFinales.append(K[opcion - 1])
        else:
            seguir = False
    F = nodosFinales
    borrarPantalla()

    conexiones = []
    print("CONEXIONES\n")
    
    seguir = True

    while(seguir):
        tupla = ("", "", "")
        mostrarNodos(K)
        nodoInicio = input("Ingrese una opción (vacío para terminar): ")

        if (nodoInicio != ""):
            nodoInicio = int(nodoInicio)

            mostrarAlfabeto(E)
            arista = input("Ingrese una opción: ")
            arista = int(arista)

            mostrarNodos(K)
            nodoFinal = input("Ingrese una opción: ")
            nodoFinal = int(nodoFinal)

            tupla = (K[nodoInicio - 1], E[arista - 1], K[nodoFinal - 1])
            conexiones.append(tupla)
        
        else:
            seguir = False

    afnd = Afnd(K, E, S, F, conexiones)
    return afnd

def menu():
    c=0
    pase="y"
    fin="y"
    ulti="y"
    relle="y"
    automata = None

    while True:
        opciones()
        opcion = None

        opcion = input("Ingrese una opcion: ")
        opcion = int(opcion)
        while (opcion < 0 or opcion > 4):
            opcion = input("Ingrese una opcion: ")
        borrarPantalla()

        if (opcion == 1):
            automata = crearAutomata()
        elif (opcion == 2):
            if (automata is None):
                print("ERROR. Primero debe ingresar un automata.")
                aux = input("Pulse ENTER para continuar...")
                borrarPantalla() 
            else:
                automata.mostrarQuintupla()
                aux = input("Pulse ENTER para continuar...")
                borrarPantalla()
        elif (opcion == 3):
            if (automata is None):
                print("ERROR. Primero debe ingresar un automata.")
                aux = input("Pulse ENTER para continuar...")
                borrarPantalla() 
            else: 
                palabra = input("Ingrese una palabra que leera el automata: ")
                afd = Afd(automata)
                afd.leer(palabra)
                aux = input("Pulse ENTER para continuar...")
                borrarPantalla()
        elif (opcion == 4):
            if (automata is None):
                print("ERROR. Primero debe ingresar un automata.")
                aux = input("Pulse ENTER para continuar...")
                borrarPantalla() 
            else:
                afd = Afd(automata)
                afd.mostrarQuintupla()
                aux = input("Pulse ENTER para continuar...")
                borrarPantalla()
        elif (opcion == 5):
            print("ERROR. No se alcanzo a implementar esta función.")
            aux = input("Pulse ENTER para continuar...")
            borrarPantalla()

def main():
    print("Grafos y lenguajes formales\n21041|INFB8061-1\n\nTrabajo 2: Automata\n")
    print("Integrantes:\n")
    print("- Felipe Flores Vivanco\n- Andres Mella\n- Jorge Verdugo Chacon\n- Javiera Vergara Navarro")
    menu()



main()
