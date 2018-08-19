from __future__ import division
import os.path
from numpy import array, ma
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def visualize(G, filename):
    # pos = nx.layout.spring_layout(G)
    #
    # node_sizes = [3 + 10 * i for i in range(len(G))]
    # M = G.number_of_edges()
    # edge_colors = range(2, M + 2)
    # edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
    #
    # nodes = nx.draw_networkx_nodes(G, pos, node_size=5,node_color='blue')
    # edges = nx.draw_networkx_edges(G, pos, arrowstyle='->',
    #                                arrowsize=2, edge_color=edge_colors,
    #                                edge_cmap=plt.cm.Blues, width=1)
    # # set alpha value for each edge
    # for i in range(M):
    #     edges[i].set_alpha(edge_alphas[i])
    #
    # ax = plt.gca()
    # ax.set_axis_off()
    # plt.savefig(os.path.basename(filename) + '.svg', bbox_inches='tight')
    # plt.close();

    # val_map = {0: 1.0,
    #        1 0.5714285714285714,
    #        2: 0.0}

    values = [G.nodes[node]['type'] for node in G.nodes()]

    nx.draw(G, cmap=plt.get_cmap('jet'), node_color=values)

    # nx.draw(G)
    plt.show()
    plt.savefig(os.path.basename(filename) + '.svg', bbox_inches='tight')
    plt.close();
