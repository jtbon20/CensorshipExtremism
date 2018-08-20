from __future__ import division
import os.path
from numpy import array, ma
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def visualize(G, pos):
    values = [G.nodes[node]['type']*100 for node in G.nodes()]

    edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())

    # node_sizes = []
    # for n,d in G.nodes(data=True):
    #     node_sizes.append( d['fitness']*5)

    plt.clf()
    # nx.draw(G, pos=pos, cmap=plt.get_cmap('Set1'), node_size = node_sizes, node_color=values, edgelist=edges, edge_color=weights, edge_size=1, edge_cmap=plt.get_cmap('RdGy'))
    nx.draw(G, pos=pos, cmap=plt.get_cmap('Set1'), node_color=values, edgelist=edges, edge_color=weights, edge_size=1, edge_cmap=plt.get_cmap('RdGy'))
    plt.draw()
    plt.pause(.0001)

    # plt.savefig(os.path.basename(filename) + '.svg', bbox_inches='tight')
