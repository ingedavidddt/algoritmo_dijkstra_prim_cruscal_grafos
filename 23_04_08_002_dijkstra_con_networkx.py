# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 22:25:47 2023

@author: david
"""

import networkx as nx
import matplotlib.pyplot as plt

# Pedir al usuario que ingrese el número de nodos que desea
num_nodos = int(input("Ingrese el número de nodos: "))

# Crear un grafo vacío
grafo = nx.Graph()

# Pedir al usuario que ingrese los nombres de los nodos
for i in range(num_nodos):
    nodo = input("Ingresa el nombre del nodo {}: ".format(i+1))
    grafo.add_node(nodo)

# Pedir al usuario que ingrese las conexiones y pesos
    
    
while True:
    entrada = input("Ingrese la conexión y su peso (o escriba 'fin' para terminar): ")
    if entrada == "fin":
        break
    else:
        conexion, peso = entrada.split('-')
        nodo1, nodo2 = conexion.split(',')
        grafo.add_edge(nodo1, nodo2, weight=int(peso))

# Dibujar el grafo original
pos = nx.spring_layout(grafo)
nx.draw(grafo, pos=pos, with_labels=True, node_size=500, font_size=12, font_weight='bold')
pesos = nx.get_edge_attributes(grafo, 'weight')
nx.draw_networkx_edge_labels(grafo, pos=pos, edge_labels=pesos)
plt.show()

# Algoritmo de Dijkstra
nodo_origen = input("Ingrese el nodo de origen: ")
nodo_destino = input("Ingrese el nodo de destino: ")


distancias, path = nx.single_source_dijkstra(grafo, nodo_origen, weight='weight')
camino = path[nodo_destino]
peso_camino = distancias[nodo_destino]



print("El camino más corto entre {} y {} es: {}".format(nodo_origen, nodo_destino, camino))
print("El peso del camino entre {} y {} es: {}".format(nodo_origen, nodo_destino, peso_camino))

# Crear un subgrafo con el camino más corto encontrado
subgrafo = grafo.subgraph(camino)

# Dibujar el camino más corto
nx.draw(subgrafo, pos, with_labels=True, edge_color='r', width=3)
pesos_subgrafo = nx.get_edge_attributes(subgrafo, 'weight')
nx.draw_networkx_edge_labels(subgrafo, pos=pos, edge_labels=pesos_subgrafo)



plt.show()




