class Afd(AutomataFinito):
    # Se crea un elemento de la tabla comenzando por la etiqueta
    def procesarNodo(nodo, AFND, tabla):
        etiquetaNodo = etiquetas(nodo)
        tabla[etiquetaNodo] = {}

        #Por cada elemento que componga el nodo, se recorre AFND para crear los conjuntos
        #de nodos a los que se puedan conectar mediante el alfabeto
        #Luego llama recursivamente la función cambiando el nodo del parámetro

        for elemento in nodo:
            for caracter in AFND[elemento].keys():
                if caracter not in tabla[etiquetaNodo]:
                    tabla[etiquetaNodo][caracter] = []
                tabla[etiquetaNodo][caracter] = combinarListas(tabla[etiquetaNodo][caracter], AFND[elemento][caracter])
                etiqueta = etiquetas(tabla[etiquetaNodo][caracter])
                if etiqueta not in tabla:
                    procesarNodoAFD(tabla[etiquetaNodo][caracter], AFND, tabla)
        return tabla