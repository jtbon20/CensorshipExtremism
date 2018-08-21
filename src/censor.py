import sys
import networkx as nx
from simulate import *

#Arguments
if len(sys.argv) < 2:
    print("Usage: %s <filename>" % sys.argv[0])
    sys.exit(1)

# Program Constants
filename = sys.argv[1]

# Simulation Constants
simulationTime = 1000

#run the simulation
runSimulations(simulationTime)
