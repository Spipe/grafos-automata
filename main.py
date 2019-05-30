#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Afnd import Afnd
from Afd import Afd

##Datos de prueba:

E=["a","b"]
'''L=[("Q0","a","Q2"),
   ("Q0","b","Q0"),
   ("Q0","","Q1"),
   ("Q1","a","Q4"),
   ("Q1","b","Q1"),
   ("Q2","a","Q0"),
   ("Q3","a","Q1"),
   ("Q4","a","Q4")]'''
#Ejemplo con el ejercicio de la prueba
L=[("Q0", "a", "Q2"),
    ("Q0", "b", "Q0"),
    ("Q0", "", "Q1"),
    ("Q2", "a", "Q0"),
    ("Q4", "a" "Q3"),
    ("Q1", "b", "Q1"),
    ("Q3", "a", "Q1"),
    ("Q1", "", "Q4"),
    ("Q1", "b", "Q1")]
K=["Q0","Q1","Q2","Q3","Q4"]
S=["Q0"]
F=["Q1"]

# Aquí comienza el main##
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

x = Afnd(K, E, S, F, L)
x.mostrarQuintupla()
z = Afd(x)
z.leer("aba")
