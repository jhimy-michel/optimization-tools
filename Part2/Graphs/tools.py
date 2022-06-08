import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import csv

def print_graph_from_adj_matrix(path):
    with open(path, 'r') as f:
        d_reader = csv.DictReader(f)
        headers = d_reader.fieldnames
    G, _, _ = get_graph_from_adjacency_matrix(path)
    labels = make_label_dict(headers[1:])
    edge_labels = dict(((u, v), d["weight"]) for u, v, d in G.edges(data=True))
    pos = nx.spring_layout(G, k=(5 / (G.order()**(1/2))), iterations=20, scale=5)
    nx.draw(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, pos, node_size=500, with_labels=True)

def make_label_dict(labels):
    l = {}
    for i, label in enumerate(labels):
        l[i] = label
    return l

def show_graph_with_labels(adjacency_matrix, mylabels):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw(gr, node_size=500, labels=mylabels, with_labels=True)
    plt.show()

def get_graph_from_adjacency_matrix(csvfile, filling_values=None):
    with open(csvfile, 'r') as f:
        ncols = len(next(f).split(','))
    x = np.genfromtxt(csvfile, delimiter=',', filling_values=filling_values, dtype='float32', names=True, usecols=range(1, ncols))
    labels = x.dtype.names
    y = x.view(dtype=('float32', len(x.dtype)))
    G = nx.from_numpy_matrix(y)
    G = nx.relabel_nodes(G, dict(zip(range(ncols - 1), labels)))
    return G, y, list(labels)