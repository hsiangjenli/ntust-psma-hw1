import pandas as pd
import numpy as np
from .graph import Graph
import operator
from copy import deepcopy

class DegreeBased:

    def __init__(self, graph: dict, degree: int or list, operation=operator.gt):

        self.graph = graph
        self.degree = degree
        self.operation = operation
        

    def sparsify(self):
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
                
                else:
                    pass

        return sparsified_graph
    
    def fit(self):
        __sparsified_graph = self.sparsify()
        __sparsified_nodes = __sparsified_graph.edges.keys()
        sparsified_graph = Graph()

        for node1 in self.graph.edges.keys():
            if node1 in __sparsified_nodes:
                for node2 in self.graph.edges[node1]:
                    if node2 in __sparsified_nodes:
                        sparsified_graph.add_edge(node1=node1, node2=node2)
        
        return sparsified_graph
    

class RandomWalk:
    
    @staticmethod
    def fit(graph: dict, node1_dropout: float=0.1, neighbor_dropout: float=0.1) -> dict:
        
        graph = deepcopy(graph)
        sparsified_graph = Graph()

        # 先將 node1_dropout 的 node1 刪除
        node1_dropout_size = int(len(graph.edges) * node1_dropout)
        node1_dropout = np.random.choice(list(graph.edges.keys()), size=node1_dropout_size, replace=False)

        for node1 in node1_dropout:
            graph.edges.pop(node1)
        
        # 再將 neighbor_dropout 的 neighbor 刪除
        for node1, neighbors in graph.edges.items():
            neighbor_remain_size = int(len(neighbors) * (1 - neighbor_dropout))
            neighbor_remain_size = 1 if neighbor_remain_size == 0 else neighbor_remain_size
            
            sparsified_graph.edges[node1] = list(
                np.random.choice(
                    neighbors, 
                    size=neighbor_remain_size, 
                    replace=False
                )
            )
        
        return sparsified_graph
            