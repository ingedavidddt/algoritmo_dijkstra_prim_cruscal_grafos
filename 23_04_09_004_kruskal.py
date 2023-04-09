# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 01:50:39 2023

@author: david
"""

import networkx as nx
import random
import matplotlib.pyplot as plt

# Crear un grafo con pesos aleatorios
G = nx.gnm_random_graph(5, 15) # Crea un grafo aleatorio con 5 nodos y 15 aristas usando el modelo G(n,m)

# Asignar pesos aleatorios a las aristas del grafo que van de 1 a 10
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(1, 10)

# Calcular Árbol de Máximo y Mínimo de Kruskal
mst_max = nx.algorithms.tree.maximum_spanning_tree(G)
mst_min = nx.algorithms.tree.minimum_spanning_tree(G)

# Imprimir los pesos de las aristas del Árbol de Máximo
print("Árbol de Máximo:")
for edge in mst_max.edges(data=True):
    print(edge)

# Imprimir los pesos de las aristas del Árbol de Mínimo
print("Árbol de Mínimo:")
for edge in mst_min.edges(data=True):
    print(edge)

# Graficar el grafo original
plt.figure()
pos = nx.spring_layout(G) # Calcular la posición de los nodos para graficar el grafo
nx.draw_networkx(G, pos) # Graficar el grafo original
edge_labels = nx.get_edge_attributes(G, 'weight') # Obtener un diccionario con los pesos de las aristas
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) # Mostrar los pesos de las aristas
plt.title("Grafo Original")
plt.show() # Mostrar la figura

# Graficar el Árbol de Máximo
plt.figure()
pos = nx.spring_layout(G) # Calcular la posición de los nodos para graficar el grafo
nx.draw_networkx(G, pos) # Graficar el grafo original
nx.draw_networkx_edges(mst_max, pos, edge_color='r', width=2) # Graficar el Árbol de Máximo
nx.draw_networkx_edge_labels(mst_max, pos, edge_labels=nx.get_edge_attributes(mst_max, 'weight')) # Etiquetar los pesos del Árbol de Máximo
plt.title("Árbol Máximo")
plt.show() # Mostrar la figura

# Graficar el Árbol de Mínimo
plt.figure()
pos = nx.spring_layout(G) # Calcular la posición de los nodos para graficar el grafo
nx.draw_networkx(G, pos) # Graficar el grafo original
nx.draw_networkx_edges(mst_min, pos, edge_color='b', width=2) # Graficar el Árbol de Mínimo
nx.draw_networkx_edge_labels(mst_min, pos, edge_labels=nx.get_edge_attributes(mst_min, 'weight'))
plt.title("Árbol Minimo")
plt.show() # Mostrar la figura
