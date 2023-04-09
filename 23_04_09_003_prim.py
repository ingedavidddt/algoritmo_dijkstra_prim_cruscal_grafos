# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 01:10:04 2023

@author: david
"""

import networkx as nx
import random
import matplotlib.pyplot as plt

# Crear un grafo con pesos aleatorios
G = nx.gnm_random_graph(5, 15) # Crea un grafo aleatorio con 10 nodos y 20 aristas usando el modelo G(n,m)

# Asignar pesos aleatorios a las aristas del grafo que van de 1 a 10
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(1, 10)

# Calcular el Árbol Parcial mínimo de Prim
T = nx.minimum_spanning_tree(G) # Calcula el Árbol Parcial mínimo de Prim del grafo G

# Dibujar el grafo y el Árbol Parcial mínimo de Prim
plt.figure(figsize=(10, 10)) # Crea una figura con tamaño 10x10
pos = nx.spring_layout(G) # Calcula las posiciones de los nodos usando el algoritmo de layout spring
nx.draw_networkx_nodes(G, pos) # Dibuja los nodos del grafo
nx.draw_networkx_edges(G, pos) # Dibuja las aristas del grafo
nx.draw_networkx_labels(G, pos) # Dibuja las etiquetas de los nodos del grafo
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u,v):d['weight'] for (u,v,d) in G.edges(data=True)}, font_size=20, font_color='green') # Dibuja las etiquetas de las aristas del grafo con los pesos, usando el tamaño de fuente de 15
nx.draw_networkx_edges(T, pos, edge_color='r', width=2) # Dibuja las aristas del Árbol Parcial mínimo de Prim con color rojo y un ancho de 2
plt.axis('off') # Oculta los ejes y los bordes del plot
plt.show() # Muestra el plot
