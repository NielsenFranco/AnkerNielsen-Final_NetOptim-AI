# network_graph.py
# Construye un grafo de ubicaciones candidatas y utilidades basicas

import networkx as nx
import math
import random

def build_grid_candidates(nx_count=5, ny_count=5, spacing=1.0):
    """Genera una grilla de candidatos (x,y)"""
    nodes = []
    for i in range(nx_count):
        for j in range(ny_count):
            nodes.append((i * spacing, j * spacing))
    return nodes

def build_random_candidates(n=25, x_max=10, y_max=10, seed=0):
    random.seed(seed)
    return [(random.uniform(0, x_max), random.uniform(0, y_max)) for _ in range(n)]

def euclidean(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def build_graph(nodes, add_backhaul_edges=True, max_dist_for_edge=None):
    G = nx.Graph()
    for idx, coord in enumerate(nodes):
        G.add_node(idx, pos=coord, install_cost= random.uniform(10,50), capacity=random.uniform(80,150))
    # agregar aristas segun distancia
    n = len(nodes)
    for i in range(n):
        for j in range(i+1, n):
            d = euclidean(nodes[i], nodes[j])
            if max_dist_for_edge is None or d <= max_dist_for_edge:
                G.add_edge(i, j, weight=d, backhaul_capacity=random.uniform(500,2000))
    return G

def get_positions(G):
    return {n: G.nodes[n]['pos'] for n in G.nodes()}

# ejemplo de uso:
if __name__ == "__main__":
    nodes = build_random_candidates(16, x_max=20, y_max=20)
    G = build_graph(nodes, max_dist_for_edge=8)
    print("Nodos:", len(G.nodes()), "Aristas:", len(G.edges()))
