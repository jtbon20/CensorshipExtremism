from __future__ import division
import os.path
from numpy import array, ma, zeros
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def visualize(G, pos):
    values = [G.nodes[node]['type']*100 for node in G.nodes()]

    edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())

    node_labels = nx.get_node_attributes(G,'type')

    node_sizes = []
    for n,d in G.nodes(data=True):
        node_sizes.append( d['fitness']*100 + 200)

    plt.clf()
    # nx.draw(G, pos=pos, cmap=plt.get_cmap('Set1'), node_size = node_sizes, node_color=values, edge_color=weights,edgelist=edges, edge_size=1, edge_cmap=plt.get_cmap('RdGy'))

    nx.draw(G, pos=pos, cmap=plt.get_cmap('Set1'), node_color=values, edgelist=edges, edge_color=weights, edge_size=1, edge_cmap=plt.get_cmap('RdGy'))
    # nx.draw(G, pos=pos, cmap=plt.get_cmap('jet'), node_color=values, edgelist=edges, edge_color=weights, edge_size=1, edge_cmap=plt.get_cmap('RdGy'))
    # nx.draw_networkx_labels(G, pos, labels = node_labels)
    plt.pause(.0001)

def heatMap(data, filename):
    plt.clf()
    plt.imshow(data, cmap=plt.get_cmap('Reds'))
    plt.savefig(os.path.basename(filename) + '.svg', bbox_inches='tight')

def save(G, filename):
    pos = nx.spring_layout(G)
    values = [G.nodes[node]['type']*100 for node in G.nodes()]

    edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())

    node_sizes = []
    for n,d in G.nodes(data=True):
        node_sizes.append( d['fitness']*200 + 100)

    plt.clf()
    nx.draw(G, pos=pos, cmap=plt.get_cmap('Set1'), node_color=values, edgelist=edges, edge_color=weights, edge_size=1, edge_cmap=plt.get_cmap('RdGy'))
    plt.savefig(os.path.basename(filename) + '.svg', bbox_inches='tight')
