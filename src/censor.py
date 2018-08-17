import sys
import networkx as nx
from plot import *
from numpy import vstack, zeros
import numpy as np

#Arguments
if len(sys.argv) < 2:
    print("Usage: %s <filename>" % sys.argv[0])
    sys.exit(1)

# Constants
filename = sys.argv[1]

# Set up arrays to store processed data

# Global Population variables
n = 100 # population
seed = 42 # for random processes
initPE = .02 # percent of population that initallally has extreme views

# General Population variables
gpEdgeProb = .05 # Probability for edge creation
gpN = int (n * (1-initPE)) # general population inital number

# Extremist Population variables
epN = int(n - gpN) # extreme population inital number
epDensity = .2 # number of groups relative to size of extreme population
epEdgeProb = .3 # probabilty of rewiring edges
epGroups = int (epDensity * epN)
epGroupSize = int (1 / epDensity)

# Initialize Graphs
gp = nx.gnp_random_graph(gpN, gpEdgeProb, seed=seed, directed=True)
ep = nx.relaxed_caveman_graph(epGroups, epGroupSize, epEdgeProb, seed=seed)

#Process data

#Print the result
visualize(gp, filename)
