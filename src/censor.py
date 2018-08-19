import sys
import networkx as nx
from plot import *
from init import *
from numpy import vstack, zeros
import numpy as np

#Arguments
if len(sys.argv) < 2:
    print("Usage: %s <filename>" % sys.argv[0])
    sys.exit(1)

# Constants
filename = sys.argv[1]

G = initializePopulation();


#Process data

#Print the result
visualize(G, filename)
