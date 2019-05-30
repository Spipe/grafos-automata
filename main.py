#!/usr/bin/env python
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
    print("(1)Si desea crear un afd/afnd. ")
    print("(2)Ingrese una palabra para comprobar e indicar si pertenece al lenguaje dela automata.")
    print("(3)Si quiere obtener el afd equivalente")
    print("(4)Si quiere obtener el afd minimo")
    print("(0) Salir.")

#Limpia la pantalla
def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def menu():
    c=0
    pase="y"
    fin="y"
    ulti="y"
    relle="y"

    while True:
        opciones()
        opcion = input("Ingrese una opcion: ")
        borrarPantalla()
        if opcion == "1":
            #Limpia pantalla
            while pase=="y":
                Letra=input("ingrese una de las letras que leera el automata:")
                E.append(Letra)
                pase=input("Desea seguir agregando letras (y/n):")

            borrarPantalla()             
            while fin=="y":
                nodo=input("Ingrese un nodo:")
                K.append(nodo)
                fin=input("Desea agregar otro nodo (y/n): ")    
            borrarPantalla()        
            while relle=="y":
                if c==0:
                    p=input("Ingrese el nodo inicial: ")
                    S.append(p)
                    c=c+1
                else:
                    p=input("Ingrese el nodo: ")
                r=input("Ingrese que letra va a leer:")
                t=input("Ingrese al nodo que se conectara:")
                tupla=p,r,t
                L.append(tupla)
                relle=input("Desea seguir agregando uniones (y/n):")
            print(L)           
            while ulti== "y":
                j=input("Ingrese un nodo de termino:")
                F.append(j)
                ulti=input("Desea seguir ingresando nodos finales (y/n): ")
            borrarPantalla() 
            aux=input("Desea ver la quintupla (y/n): ")
            #Inicializa los objetos despues de ingresar los datos respectivos 
            var_afnd = Afnd(K, E, S, F, L)
            var_afd = Afd(var_afnd) 
            if(aux=="y"):
                var_afnd.mostrarQuintupla()
                aux_1=input("Pulse cualquier letra para continuar...")
            borrarPantalla() 
        
        if opcion == "2":
            dato=input("Ingrese una palabra: ")
            var_afd.leer(dato)
            aux=input("Pulse cualquier letra para continuar...")
            borrarPantalla() 

        elif opcion == "3":
            ver=input("Desea ver la quintupla del AFD (y/n): ")
            if(ver=="y"):
                var_afd.mostrarQuintupla()
            aux=input("Pulse cualquier letra para continuar...")
            borrarPantalla()     
        elif opcion == "4":
            print("Opcion 4")
            aux=input("Pulse cualquier letra para continuar...")
            borrarPantalla() 
        elif opcion == "0":
            break

def main():
    print("Grafos y lenguajes formales\n21041|INFB8061-1\n\nTrabajo 2: Automata\n")
    print("Integrantes:\n")
    print("- Felipe Flores Vivanco\n- Andres Mella\n- Jorge Verdugo Chacon\n- Javiera Vergara Navarro")
    menu()



main()
