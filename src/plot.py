from __future__ import division
import os.path
from numpy import array, ma
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def visualize(G, filename):
    values = [G.nodes[node]['type'] for node in G.nodes()]

    edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())

    plt.clf()
    nx.draw(G, cmap=plt.get_cmap('jet'), node_color=values, edgelist=edges, edge_color=weights, edge_cmap=plt.get_cmap('RdGy'))
    plt.draw()
    plt.pause(.000005)
    # plt.savefig(os.path.basename(filename) + '.svg', bbox_inches='tight')


# def save(G, filename):
#     values = [G.nodes[node]['type'] for node in G.nodes()]
#
#     edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())
#
#     nx.draw(G, cmap=plt.get_cmap('jet'), node_color=values, edgelist=edges, edge_color=weights, edge_cmap=plt.get_cmap('RdGy'))
#     plt.savefig(os.path.basename(filename) + '.svg', bbox_inches='tight')
