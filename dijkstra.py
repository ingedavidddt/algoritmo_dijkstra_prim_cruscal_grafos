# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:07:56 2023

@author: david
"""
import math
import tkinter as tk

class WeightedGraph():
    # Constructor, por defecto crea un diccionario vacío
    # El grafo se presenta como un diccionario de la forma
    # {nodo: [arcos]}
    # arcos es una lista de los nodos adyacentes 
    def __init__(self, graph={}):
        self.graph = graph

    # Devuelve una representación formal del contenido del grafo
    def __repr__(self):
        nodes = ''
        for node, edges in self.graph.items():
            nodes += f'{node}: {edges}\n'
        return nodes

    # Iterador para recorrer todos los nodos del grafo
    def __iter__(self):
        self.iter_obj = iter(self.graph)
        return self.iter_obj

    # Devuelve los nodos del grafo como una lista
    def nodes(self):
        return list(self.graph.keys())

    # Devuelve los arcos del grafo como una lista de tuplas
    # (nodo_origen, nodo_destino)
    def edges(self, node=None):
        if node:
            if self.existNode(node):
                return [(node, e) for e in self.graph[node]]
            else:
                return []
        else:
            return [(n, e) for n in self.graph.keys() for e in self.graph[n]]

    # Devuelve una lista de los nodos aislados
    def isolatedNodes(self):
        return [node for node in self.graph if not self.graph[node]]



    # Inserta un nodo en el grafo
    def addNode(self, node):
        # Si el nodo no está en el grafo,
        # se añade al diccionario con una lista vacía 
        if node not in self.graph:
            self.graph[node] = []   # nodo aislado

    # Elimina un nodo del grafo
    # Primero elimina todos los arcos del nodo
    def removeNode(self, node):
        if node in self.graph:
            edges = list(self.graph[node])
            for edge in edges:
                self.removeEdge((node, edge))
            self.graph.pop(node)

    # Inserta una arco entre los nodos indicados
    # El arco es una lista con los nodos que une
    # Si no existe el nodo lo inserta
    def addEdge(self, edge, weight):
        n1, n2 = tuple(edge)
        for n, e in [(n1, n2), (n2, n1)]:
            if n in self.graph:
                if e not in self.graph[n]:
                    self.graph[n].append((e, weight))
                    if n == e:
                        break       
            else:
                self.graph[n] = [(e, weight)] 

    # Elimina un arco entre nodos
    # El arco es una lista con los nodos que une
    def removeEdge(self, edge):
        n1, n2 = tuple(edge)
        for n, e in [(n1, n2), (n2, n1)]:
            if n in self.graph:
                if e in self.graph[n]:
                    self.graph[n].remove(e)

  

    # Devuelve todos los caminos entre dos nodos
    def findPaths(self, start, end, path = []):
        if start not in self.graph or end not in self.graph:
            return []
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node, _ in self.graph[start]:       # para cada nodo adyacente
            if node not in path:
                newpaths = self.findPaths(node, end, path)
                for subpath in newpaths:
                    paths.append(subpath)
        return paths

    # Devuelve el camino más corto entre dos nodos
    # camino más corto == el de menor peso
    # Algoritmo de Dijkstra para grafos ponderados
  
    def shortestPath(self, start, end):
        INF = float('inf')
        # Diccionario de nodos con un peso infinito
        unvisited = {node: INF for node in self.graph.keys()}
        # Diccionario de predecesores
        predecessor = {node: node for node in self.graph.keys()}
        
        visited = {}
        current = start
        currentWeight = 0
        unvisited[current] = currentWeight      # nodo origen peso 0
        while True:
            for node, weight in self.graph[current]:
                if node not in unvisited:
                    continue                    # nodo ya tratado
                newWeight = currentWeight + weight
                if unvisited[node] > newWeight:
                    # Tomar el nodo con el menor peso
                    unvisited[node] = newWeight
                    predecessor[node] = current # predecesor con el menor peso
            visited[current] = currentWeight    # visitado con el menor peso 
            unvisited.pop(current)              # eliminar de los no visitados
            if not unvisited:
                break       # Terminar el bucle si no hay nodos por visitar
            # Tomar el nodo con el menor peso de los no visitados
            candidates = [(n, w) for n, w in unvisited.items() if w != INF]
            current, currentWeight = sorted(candidates, key = lambda x: x[1])[0]
        # Reconstrucción del camino de longitud mínima
        # Se parte del nodo final al inicial
        path = []
        node = end
        while True:
            path.append(node)
            if(node == predecessor[node]):
                break
            node = predecessor[node]
        # Devuelve una tupla con el camino y el peso total
        return (path[::-1], visited[end])
    
    
    
    
    
    # Consulta si el grafo está vacío
    def isEmpty(self):
        return self.graph == {}

    # Consulta si el nodo existe en el grafo
    def existNode(self, node):
        return node in self.graph.keys()

    # Consulta si el arco existe en el grafo
    def existEdge(self, edge):
        n1, n2 = tuple(edge)
        return (n1, n2) in self.edges(n1) or (n2, n1) in self.edges(n2)
    




# Grafo ejemplo con listas de adyacencia y pesos asociados
grafo = {'A': [('B', 1), ('C', 2), ('D', 3)],
         'B': [('A', 1), ('C', 4)],
         'C': [('A', 2), ('B', 4), ('D', 5)],
         'D': [('A', 3), ('C', 5)]}
ruta = []
 

nodos_resaltados = []
color_nodos_resaltados = 'blue'
color_conexiones_resaltadas = 'blue'

def graficar(nodos_resaltados):
    # Calcular la posición de cada nodo
    posiciones = {}
    total_nodos = len(grafo)
    for i, nodo in enumerate(grafo.keys()):
        angulo = 2 * math.pi * i / total_nodos
        x = math.cos(angulo)
        y = math.sin(angulo)
        posiciones[nodo] = (x, y)

    # Inicializar la ventana
    ventana = tk.Tk()
    ventana.title('Grafo')

    # Inicializar el canvas
    canvas = tk.Canvas(ventana, width=500, height=500, bg='white')
    canvas.pack()

   

    for origen, destinos in grafo.items():
        for destino, peso in destinos:
            x1, y1 = posiciones[origen]
            x2, y2 = posiciones[destino]
            
            canvas.create_text(250 + (x1 + x2) * 100, 250 - (y1 + y2) * 100,
                               text=str(peso), font=('Arial', 14), fill='red')
            



            if origen in nodos_resaltados and destino in nodos_resaltados:
                canvas.create_line(250 + x1 * 200, 250 - y1 * 200,
                                   250 + x2 * 200, 250 - y2 * 200,
                                   arrow=tk.NONE, fill=color_conexiones_resaltadas)
            else:
                canvas.create_line(250 + x1 * 200, 250 - y1 * 200,
                                   250 + x2 * 200, 250 - y2 * 200,
                                   arrow=tk.NONE)



    # Dibujar los nodos
    for nodo, posicion in posiciones.items():
        x, y = posicion
        if nodo in nodos_resaltados:
            canvas.create_oval(245 + x * 200, 245 - y * 200,
                               275 + x * 200, 275 - y * 200,
                               fill='white', outline=color_nodos_resaltados)
        else:
            canvas.create_oval(245 + x * 200, 245 - y * 200,
                               275 + x * 200, 275 - y * 200,
                               fill='white')
            
            
        canvas.create_text(260 + x * 200, 260 - y * 200,
                           text=nodo, fill='black')
        
   
g = WeightedGraph(grafo)    # Crear el grafo con el diccionario de ejemplo


def agregar_nodo():
    origen = entrada_origen.get()
    destino = entrada_destino.get()
    peso = int(entrada_peso.get())
    g.addEdge((origen, destino), peso)
   
    entrada_origen.delete(0, tk.END)
    entrada_destino.delete(0, tk.END)
    entrada_peso.delete(0, tk.END)
    s =[]
    graficar(s)
    
def eliminar_nodo():
    eliminar = nodo_eliminar.get()
    g.removeNode(eliminar)           # Eliminar nodo
    nodo_eliminar.delete(0, tk.END)
    s =[]
    graficar(s)
    
def eliminar_arco():
    
    origen = eliminar_origen.get()
    destino = eliminar_destino.get()
    
    g.removeEdge([origen, destino])    # Eliminar arco
    
    eliminar_origen.delete(0, tk.END)
    eliminar_destino.delete(0, tk.END)
    s =[]
    graficar(s)
    
def dijkstra():
    origen = dijkstra_origen.get()
    destino = dijkstra_destino.get()
    path, weight = g.shortestPath(origen, destino)
   
    nodos_resaltados = path
    dijkstra_peso.insert(0, str(weight))
    graficar(nodos_resaltados)

    
# Inicializar la ventana
botones = tk.Tk()
botones.title('botones')


# Inicializar los campos de entrada de texto
label_origen = tk.Label(botones, text='agregar nodo o conexion')
label_origen.grid(row=0, column=1)


# Inicializar los campos de entrada de texto
label_origen = tk.Label(botones, text='Origen:')
label_origen.grid(row=1, column=0)
entrada_origen = tk.Entry(botones)
entrada_origen.grid(row=1, column=1)

label_destino = tk.Label(botones, text='Destino:')
label_destino.grid(row=2, column=0)
entrada_destino = tk.Entry(botones)
entrada_destino.grid(row=2, column=1)

label_peso = tk.Label(botones, text='Peso:')
label_peso.grid(row=3, column=0)
entrada_peso = tk.Entry(botones)
entrada_peso.grid(row=3, column=1)

# Inicializar el botón "Agregar"
boton_agregar = tk.Button(botones, text='Agregar', command=agregar_nodo)
boton_agregar.grid(row=4, column=1)

# Inicializar los campos de entrada de texto
label_eliminar = tk.Label(botones, text='eliminar nodo')
label_eliminar.grid(row=5, column=1)
   
label_peso = tk.Label(botones, text='nodo a eliminar')
label_peso.grid(row=6, column=0)
nodo_eliminar = tk.Entry(botones)
nodo_eliminar.grid(row=6, column=1)

# Inicializar el botón "eliminar nodo"
boton_eliminar = tk.Button(botones, text='Eliminar nodo', command=eliminar_nodo)
boton_eliminar.grid(row=7, column=1)

# Inicializar los campos de entrada de texto para eliminar conexiones
label_destino_eliminar = tk.Label(botones, text='nodos a desconectar')
label_destino_eliminar.grid(row=8, column=1)

label_origen_eliminar = tk.Label(botones, text='Origen:')
label_origen_eliminar.grid(row=9, column=0)
eliminar_origen = tk.Entry(botones)
eliminar_origen.grid(row=9, column=1)



label_destino_eliminar = tk.Label(botones, text='Destino:')
label_destino_eliminar.grid(row=10, column=0)
eliminar_destino = tk.Entry(botones)
eliminar_destino.grid(row=10, column=1)



# Inicializar el botón "eliminar conexion"

boton_eliminar = tk.Button(botones, text='Eliminar conexion', command=eliminar_arco)
boton_eliminar.grid(row=11, column=1)

#botones para realizar las operaciones





label_origen_dijkstra = tk.Label(botones, text='configuracion de algoritmo de dijkstra')
label_origen_dijkstra.grid(row=12, column=1)

# Inicializar los campos de entrada de texto para configurar nodos para el algoritmo dikstra
label_origen_dijkstra = tk.Label(botones, text='Origen:')
label_origen_dijkstra.grid(row=13, column=0)
dijkstra_origen = tk.Entry(botones)
dijkstra_origen.grid(row=13, column=1)

label_destino_dijkstra = tk.Label(botones, text='Destino:')
label_destino_dijkstra.grid(row=14, column=0)
dijkstra_destino = tk.Entry(botones)
dijkstra_destino.grid(row=14, column=1)

label_peso = tk.Label(botones, text='Peso:')
label_peso.grid(row=15, column=0)
dijkstra_peso = tk.Entry(botones)
dijkstra_peso.grid(row=15, column=1)

# Inicializar el botón "dijkstra"
boton_dijkstra = tk.Button(botones, text='dijkstra', command=dijkstra)
boton_dijkstra.grid(row=16, column=1)




graficar(nodos_resaltados)
# Ejecutar la ventana
botones.mainloop()    