import networkx as nx
import matplotlib.pyplot as plt

# If you want to test out explicitly

""" G = nx.MultiDiGraph()

G.add_edge(1,2)

G.add_edge(2,3)

G.add_edge(3,1)

nx.draw_spring(G, with_labels = True)
plt.show() """


# If you want to test out with edge lists

""" edge_list = [(1,2),(2,3),(3,2)]

G = nx.MultiDiGraph
G.add_edges_from(edge_list)

nx.draw_spring(G, with_labels = True)
plt.show() """


# If you want to test out with adj matrix

""" import numpy as np

G = nx.from_numpy_array(np.array([[0,1,0],[1,1,1],[0,0,0]]))

nx.draw_spring(G, with_labels = True)
plt.show()
 """

#If you want complete graphs G = nx.complete_graph(5)
#planar graphs require no intersecting edges
#spectral graph theory works off the Laplacian
#prefer using spring method to trace graphs
#to see info on graph print(dict(G.degree)[3]) 
#to see shortest path, print(nx.shortest_path(G, start, end))
#to see node centrality, print(nx.degree_centrality(G)), refer other centrality types in readme.md 


# to connect two graph islands

""" import numpy as np
G1 = nx.complete_graph(4)
G2 = nx.complete_graph(3)
G2 = nx.relabel_nodes(G2, {0:"a", 1:"b", 2:"c"})
G_connector = nx.from_edgelist([(3, "x"),("x", "b")])

G = nx.compose_all([G1,G2, G_connector])
nx.draw_spring(G, with_labels = True)
plt.show() """
