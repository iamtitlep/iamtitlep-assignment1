""" water_bfgs.py """
import uninformed1
import water1
from node1 import print_solution

n, c  = uninformed1.breadth_first_graph_search(water1)
print_solution(n)
print("No. of visited nodes =", c)
