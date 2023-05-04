import pandas as pd
import numpy as np
from .graph import Graph
import operator

class DegreeBased:

    def __init__(self, graph: dict, degree: int or list, operation=operator.gt):

        self.graph = graph
        self.degree = degree
        self.operation = operation
        

    def fit(self):
        """
        Sparsify the graph by degree.
        """
        sparsified_graph = Graph()

        for node1, neighbors in self.graph.edges.items():
            
            if isinstance(self.degree, list):
                if len(neighbors) in self.degree:
                    sparsified_graph.edges[node1] = neighbors
            
            elif isinstance(self.degree, int):
                if self.operation(len(neighbors), self.degree):
                    sparsified_graph.edges[node1] = neighbors

        return sparsified_graph