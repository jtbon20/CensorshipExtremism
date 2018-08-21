import sys
import networkx as nx
from simulate import *
import numpy as np
from numpy import zeros

#Arguments
if len(sys.argv) < 2:
    print("Usage: %s <filename>" % sys.argv[0])
    sys.exit(1)

# Program Constants
filename = sys.argv[1]

# Simulation Constants
simulationTime = 1000

#run the simulation
data = runSimulations(simulationTime)

#plot the data
heatMap(data, filename)
