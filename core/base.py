from typing import NewType
import warnings

nodeId = NewType('nodeId', int)
graph = NewType('graph', dict)

class BaseGraph:

    def __init__(self):
        self.edges = {}
    
    @property
    def nodes(self) -> list:
        """_summary_

        Get all nodes of the graph.

        Returns
        -------
        list
            A list of node ids of the nodes.
        """
        
        # return list(self.edges.keys())
        return list(set(sum(self.edges.values(), [])) | set(self.edges.keys()))

    @property
    def average_degree(self):
        """_summary_

        Get the average degree of the graph.

        Returns
        -------
        float
            The average degree of the graph.
        """
        
        return sum([len(self.edges[node]) for node in self.edges]) / len(self.edges)
    
# class BaseSparsification:
#     def __init__(self, graph: graph) -> None:
#         self.graph = graph

def if_node_not_exist(func):
    
    def wrapper(*args, **kwargs):
        
        try:
            return func(*args, **kwargs)
        
        except Exception as e:
            warnings.warn(f"func({func.__name__}): The node {e} does not exist.")
            return 0
            
        
    return wrapper
