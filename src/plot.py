from __future__ import division
import os.path
from numpy import array, ma
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def visualize(G, filename):
    values = [G.nodes[node]['type'] for node in G.nodes()]

    nx.draw(G, cmap=plt.get_cmap('jet'), node_color=values)

    plt.show()
    plt.savefig(os.path.basename(filename) + '.svg', bbox_inches='tight')
    plt.close();
